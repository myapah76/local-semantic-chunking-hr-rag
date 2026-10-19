import re
from typing import List, Dict, Any, Optional
from baselines.base import BaseChunker, Chunk

class SentenceChunker(BaseChunker):
    """
    Sentence-based Chunking (Baseline 2):
    Segments document into sentences, then bundles N consecutive sentences per chunk
    with an optional sentence overlap to preserve local context.
    """
    def __init__(self, sentences_per_chunk: int = 3, sentence_overlap: int = 1):
        super().__init__(name=f"SentenceBased(N={sentences_per_chunk},overlap={sentence_overlap})")
        self.sentences_per_chunk = sentences_per_chunk
        self.sentence_overlap = sentence_overlap

    def _split_into_sentences(self, text: str) -> List[str]:
        # Handle punctuation, newlines, and bullet points
        raw_sentences = re.split(r'(?<=[.!?])\s+|\n+', text)
        sentences = [s.strip() for s in raw_sentences if s.strip()]
        return sentences

    def chunk(self, text: str, doc_id: str, metadata: Optional[Dict[str, Any]] = None) -> List[Chunk]:
        sentences = self._split_into_sentences(text)
        if not sentences:
            return []

        chunks: List[Chunk] = []
        step = max(1, self.sentences_per_chunk - self.sentence_overlap)
        chunk_idx = 0

        for i in range(0, len(sentences), step):
            window = sentences[i : i + self.sentences_per_chunk]
            content = " ".join(window).strip()
            if content:
                chunks.append(Chunk.create(doc_id, chunk_idx, content, self.name, metadata))
                chunk_idx += 1
            if i + self.sentences_per_chunk >= len(sentences):
                break

        return chunks
