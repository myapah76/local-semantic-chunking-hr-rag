import os
import sys
import uuid
import logging
from typing import List, Dict, Any, Optional

# Ensure project root is in PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from baselines.base import BaseChunker, Chunk
from baselines.fixed_size_chunker import FixedSizeChunker
from baselines.sentence_chunker import SentenceChunker
from baselines.paragraph_chunker import ParagraphChunker
from baselines.semantic_chunker import LocalSemanticChunker
from evaluation.retriever import InMemVectorRetriever
from storage.db import get_engine, init_db, SessionLocal
from storage.models import DocumentChunk, ChunkEmbedding
from data.data_loader import DataLoader
from sqlalchemy import select, text
from config import config

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def chunk_and_store_document(
    doc_id: str,
    text_content: str,
    metadata: Optional[Dict[str, Any]] = None,
    chunker: Optional[BaseChunker] = None,
    db_session = None
) -> List[DocumentChunk]:
    """
    1. Splits document text using the given chunker (defaults to LocalSemanticChunker).
    2. Generates embeddings using the embedding model (qwen3-embedding:0.6b via Ollama).
    3. Saves chunks into 'document_chunks' table and vectors into 'chunk_embeddings' table (pgvector).
    """
    if chunker is None:
        chunker = LocalSemanticChunker()

    if metadata is None:
        metadata = {}

    # Step 1: Chunking
    chunks: List[Chunk] = chunker.chunk(text_content, doc_id=doc_id, metadata=metadata)
    if not chunks:
        logger.warning(f"No chunks produced for document {doc_id}")
        return []

    # Step 2: Compute Embeddings
    retriever = InMemVectorRetriever()
    texts = [c.content for c in chunks]
    embeddings = retriever._get_ollama_batch_embeddings(texts)

    # Convert doc_id to valid UUID
    try:
        doc_uuid = uuid.UUID(doc_id)
    except Exception:
        doc_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, doc_id)

    # Step 3: Store in PostgreSQL
    own_session = False
    if db_session is None:
        db_session = SessionLocal()
        own_session = True

    try:
        # Clear previous chunks for this document and strategy if any
        existing_chunk_ids = select(DocumentChunk.id).filter(
            DocumentChunk.document_id == doc_uuid,
            DocumentChunk.strategy == chunker.name
        )
        db_session.query(ChunkEmbedding).filter(ChunkEmbedding.chunk_id.in_(existing_chunk_ids)).delete(synchronize_session=False)
        db_session.query(DocumentChunk).filter(
            DocumentChunk.document_id == doc_uuid,
            DocumentChunk.strategy == chunker.name
        ).delete(synchronize_session=False)
        db_session.commit()

        stored_chunks = []
        for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
            chunk_record = DocumentChunk(
                document_id=doc_uuid,
                chunk_index=i,
                content=chunk.content,
                token_count=chunk.token_count,
                metadata_=metadata,
                strategy=chunker.name
            )
            db_session.add(chunk_record)
            db_session.flush()

            emb_record = ChunkEmbedding(
                chunk_id=chunk_record.id,
                embedding=emb,
                model_name=retriever.model_name
            )
            db_session.add(emb_record)
            stored_chunks.append(chunk_record)

        db_session.commit()
        logger.info(f"Successfully chunked & stored doc {doc_id} with strategy '{chunker.name}': {len(stored_chunks)} chunks saved to DB.")
        return stored_chunks

    except Exception as e:
        db_session.rollback()
        logger.error(f"Failed to store chunks for document {doc_id}: {e}")
        raise e
    finally:
        if own_session:
            db_session.close()

def search_pgvector(query: str, top_k: int = 5, strategy: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Directly query PostgreSQL pgvector using Cosine Distance (<=>),
    optionally filtered by chunking strategy.
    """
    retriever = InMemVectorRetriever()
    query_vector = retriever._get_ollama_embedding(query)
    vec_literal = "[" + ",".join(str(x) for x in query_vector) + "]"

    query_sql = text("""
        SELECT 
            dc.id,
            dc.document_id,
            dc.chunk_index,
            dc.content,
            dc.metadata,
            dc.strategy,
            ce.embedding <=> :query_vec AS cosine_distance
        FROM document_chunks dc
        JOIN chunk_embeddings ce ON dc.id = ce.chunk_id
        WHERE (:strategy IS NULL OR dc.strategy ILIKE '%' || :strategy || '%')
        ORDER BY ce.embedding <=> :query_vec ASC
        LIMIT :top_k
    """)

    session = SessionLocal()
    try:
        results = session.execute(
            query_sql, 
            {"query_vec": vec_literal, "top_k": top_k, "strategy": strategy}
        ).fetchall()
        output = []
        for r in results:
            output.append({
                "chunk_id": str(r.id),
                "document_id": str(r.document_id),
                "chunk_index": r.chunk_index,
                "strategy": r.strategy,
                "content": r.content,
                "metadata": r.metadata,
                "cosine_distance": float(r.cosine_distance),
                "similarity_score": round(1.0 - float(r.cosine_distance), 4)
            })
        return output
    finally:
        session.close()

def get_default_chunkers() -> List[BaseChunker]:
    """Return all 4 benchmark chunking strategies configured in config.py."""
    return [
        LocalSemanticChunker(similarity_threshold=config.semantic_breakpoint_threshold, min_chunk_size=config.semantic_min_chunk_size),
        FixedSizeChunker(chunk_size=config.fixed_chunk_size, chunk_overlap=config.fixed_chunk_overlap),
        SentenceChunker(sentences_per_chunk=config.sentence_batch_size, sentence_overlap=config.sentence_overlap),
        ParagraphChunker(min_paragraph_chars=config.paragraph_min_chars, max_paragraph_chars=config.paragraph_max_chars)
    ]

def import_documents(
    doc_type: Optional[str] = None, 
    chunkers: Optional[List[BaseChunker]] = None
) -> int:
    """
    Batch import documents into PostgreSQL pgvector.
    :param doc_type: Filter by 'JD', 'CV', 'POLICY', or None for all.
    :param chunkers: List of chunkers to apply. Defaults to all 4 chunking strategies.
    :return: Total number of chunks saved.
    """
    init_db()
    loader = DataLoader()
    if doc_type:
        docs = loader.get_documents_by_type().get(doc_type.upper(), [])
    else:
        docs = loader.load_all_documents()

    if chunkers is None:
        chunkers = get_default_chunkers()

    category_name = doc_type.upper() if doc_type else "ALL CATEGORIES"
    logger.info(f"Importing {len(docs)} documents ({category_name}) with {len(chunkers)} chunking strategies...")

    grand_total = 0
    db_session = SessionLocal()
    try:
        for chunker in chunkers:
            logger.info(f"=== Strategy: {chunker.name} ===")
            strat_total = 0
            for doc in docs:
                stored = chunk_and_store_document(
                    doc_id=doc.doc_id,
                    text_content=doc.content,
                    metadata={**doc.metadata, "title": doc.title, "doc_type": doc.doc_type.value},
                    chunker=chunker,
                    db_session=db_session
                )
                strat_total += len(stored)
            logger.info(f"Finished strategy '{chunker.name}': saved {strat_total} chunks.")
            grand_total += strat_total
    finally:
        db_session.close()

    logger.info(f"DONE! Successfully imported total {grand_total} chunks into PostgreSQL pgvector.")
    return grand_total

def import_all_sample_data():
    """Batch import all documents across all 4 chunking strategies."""
    return import_documents(doc_type=None, chunkers=get_default_chunkers())

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="HR Document Chunking & DB Storage Tool")
    parser.add_argument("--import-all", action="store_true", help="Batch chunk and save ALL sample documents (CV, JD, Policy) across all chunkers to DB")
    parser.add_argument("--import-jds", action="store_true", help="Batch chunk and save ALL JDs across all chunkers to DB")
    parser.add_argument("--doc-type", type=str, default=None, help="Filter document type ('JD', 'CV', 'POLICY')")
    parser.add_argument("--strategy", type=str, default=None, help="Specific chunking strategy or filter (e.g. 'Local Semantic Chunking')")
    parser.add_argument("--search", type=str, help="Search similar chunks directly from PostgreSQL pgvector")
    parser.add_argument("--top-k", type=int, default=5, help="Number of results to return")
    args = parser.parse_args()

    if args.import_all or args.import_jds:
        target_doc_type = "JD" if args.import_jds else args.doc_type
        if args.strategy:
            # Match single chunker if specified
            all_c = get_default_chunkers()
            selected_c = [c for c in all_c if args.strategy.lower() in c.name.lower()]
            if not selected_c:
                print(f"Error: Unknown strategy '{args.strategy}'. Available: {[c.name for c in all_c]}")
                sys.exit(1)
            import_documents(doc_type=target_doc_type, chunkers=selected_c)
        else:
            import_documents(doc_type=target_doc_type, chunkers=get_default_chunkers())

    elif args.search:
        results = search_pgvector(args.search, top_k=args.top_k, strategy=args.strategy)
        strat_info = f" [Strategy: {args.strategy}]" if args.strategy else " [All Strategies]"
        print(f"\nTop {len(results)} chunks matching '{args.search}'{strat_info}:\n")
        for i, res in enumerate(results, start=1):
            print(f"[{i}] Similarity: {res['similarity_score']} (Distance: {res['cosine_distance']}) | Strategy: {res['strategy']}")
            print(f"    Doc ID: {res['document_id']} (Chunk #{res['chunk_index']})")
            print(f"    Content: {res['content'][:150]}...\n")
    else:
        parser.print_help()
