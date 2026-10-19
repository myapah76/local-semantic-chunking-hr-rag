from enum import Enum
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field

class DocumentType(str, Enum):
    CV = "CV"
    JD = "JD"
    POLICY = "POLICY"

@dataclass
class HRDocument:
    doc_id: str
    doc_type: DocumentType
    title: str
    content: str
    language: str = "vi"  # 'vi', 'en', 'bilingual'
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if isinstance(self.doc_type, str):
            self.doc_type = DocumentType(self.doc_type)

@dataclass
class GroundTruthQuery:
    query_id: str
    query: str
    doc_type: DocumentType
    target_doc_id: str
    ground_truth_snippets: List[str]
    description: Optional[str] = None
    difficulty: str = "medium"  # 'easy', 'medium', 'hard'

    def __post_init__(self):
        if isinstance(self.doc_type, str):
            self.doc_type = DocumentType(self.doc_type)
