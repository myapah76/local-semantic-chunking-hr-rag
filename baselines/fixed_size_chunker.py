from typing import List, Dict, Any, Optional
from baselines.base import BaseChunker, Chunk

class FixedSizeChunker(BaseChunker):
    """
    Fixed-size Chunking (Baseline 1):
    Splits text into chunks of roughly N characters/tokens with a fixed sliding window overlap.
    Ensures words are not severed in the middle.
    """
    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 100):
        super().__init__(name=f"FixedSize(size={chunk_size},overlap={chunk_overlap})")
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk(self, text: str, doc_id: str, metadata: Optional[Dict[str, Any]] = None) -> List[Chunk]:
        clean_text = " ".join(text.split())
        if not clean_text:
            return []

        chunks: List[Chunk] = []
        start = 0
        text_len = len(clean_text)
        chunk_idx = 0

        while start < text_len:
            end = start + self.chunk_size
            if end >= text_len:
                chunk_str = clean_text[start:text_len]
                if chunk_str.strip():
                    chunks.append(Chunk.create(doc_id, chunk_idx, chunk_str, self.name, metadata))
                break

            # Adjust end to avoid severing a word
            boundary = clean_text.rfind(" ", start, end)
            if boundary != -1 and boundary > start:
                end = boundary

            chunk_str = clean_text[start:end].strip()
            if chunk_str:
                chunks.append(Chunk.create(doc_id, chunk_idx, chunk_str, self.name, metadata))
                chunk_idx += 1

            # Advance window with overlap
            next_start = end - self.chunk_overlap
            if next_start <= start:
                next_start = end
            start = next_start

        return chunks
