from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
import uuid

@dataclass
class Chunk:
    id: str
    doc_id: str
    chunk_index: int
    content: str
    char_count: int
    token_count: int
    metadata: Dict[str, Any] = field(default_factory=dict)
    strategy: str = ""

    @classmethod
    def create(cls, doc_id: str, chunk_index: int, content: str, strategy: str, metadata: Optional[Dict[str, Any]] = None) -> "Chunk":
        return cls(
            id=str(uuid.uuid4()),
            doc_id=doc_id,
            chunk_index=chunk_index,
            content=content.strip(),
            char_count=len(content.strip()),
            token_count=len(content.strip().split()),
            metadata=metadata or {},
            strategy=strategy
        )

class BaseChunker(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def chunk(self, text: str, doc_id: str, metadata: Optional[Dict[str, Any]] = None) -> List[Chunk]:
        """Split input document text into a list of Chunk objects."""
        pass
