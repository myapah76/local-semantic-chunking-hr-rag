import os
from dataclasses import dataclass
from typing import List

@dataclass
class Config:
    # Ollama / Embedding Settings
    ollama_base_url: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    embedding_model: str = os.getenv("OLLAMA_EMBEDDING_MODEL", "qwen3-embedding:0.6b")
    embedding_dim: int = 1024
    embedding_batch_size: int = 50
    embedding_timeout: int = 60

    # Semantic Chunker Settings
    semantic_breakpoint_threshold: float = 0.85  # Percentile or cosine threshold
    semantic_min_chunk_size: int = 50            # Minimum characters per chunk

    # Fixed Size Chunker Settings
    fixed_chunk_size: int = 500                  # Character/token length
    fixed_chunk_overlap: int = 100               # Overlap length

    # Sentence Chunker Settings
    sentence_batch_size: int = 3                 # Sentences per chunk
    sentence_overlap: int = 1                    # Sentence overlap

    # Evaluation Settings
    top_k_values: List[int] = (3, 5, 10)
    data_dir: str = os.path.join(os.path.dirname(__file__), "data")
    reports_dir: str = os.path.join(os.path.dirname(__file__), "reports")

config = Config()
