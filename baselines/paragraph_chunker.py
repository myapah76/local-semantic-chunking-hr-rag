import re
from typing import List, Dict, Any, Optional
from baselines.base import BaseChunker, Chunk

class ParagraphChunker(BaseChunker):
    """
    Paragraph-based Chunking (Baseline 3):
    Splits text along natural structural boundaries (double line breaks, section headers, bullet groups).
    Merges very short adjacent paragraphs to maintain contextual richness.
    """
    def __init__(self, min_paragraph_chars: int = 100, max_paragraph_chars: int = 1000):
        super().__init__(name=f"ParagraphBased(min={min_paragraph_chars},max={max_paragraph_chars})")
        self.min_chars = min_paragraph_chars
        self.max_chars = max_paragraph_chars

    def chunk(self, text: str, doc_id: str, metadata: Optional[Dict[str, Any]] = None) -> List[Chunk]:
        raw_paragraphs = re.split(r'\n\s*\n', text)
        cleaned = [p.strip() for p in raw_paragraphs if p.strip()]
        if not cleaned:
            return []

        merged: List[str] = []
        current = ""

        for p in cleaned:
            if not current:
                current = p
            elif len(current) + len(p) + 2 <= self.max_chars:
                current += "\n\n" + p
            else:
                merged.append(current)
                current = p

        if current:
            merged.append(current)

        chunks: List[Chunk] = []
        for idx, content in enumerate(merged):
            chunks.append(Chunk.create(doc_id, idx, content, self.name, metadata))

        return chunks
