-- Initialize pgvector extension and UUID generator
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Table to store document chunks
CREATE TABLE IF NOT EXISTS document_chunks (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    document_id UUID NOT NULL,
    chunk_index INTEGER NOT NULL,
    content TEXT NOT NULL,
    token_count INTEGER,
    metadata JSONB DEFAULT '{}'::jsonb,
    strategy VARCHAR(100) DEFAULT 'LocalSemantic',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store dense vector embeddings (1024 dimensions for qwen3-embedding:0.6b)
CREATE TABLE IF NOT EXISTS chunk_embeddings (
    chunk_id UUID PRIMARY KEY REFERENCES document_chunks(id) ON DELETE CASCADE,
    embedding vector(1024) NOT NULL,
    model_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create HNSW index for high-speed approximate nearest neighbor cosine search
CREATE INDEX IF NOT EXISTS idx_chunk_embeddings_hnsw 
ON chunk_embeddings USING hnsw (embedding vector_cosine_ops);

-- Index for fast lookup by document_id
CREATE INDEX IF NOT EXISTS idx_document_chunks_doc_id 
ON document_chunks (document_id);
