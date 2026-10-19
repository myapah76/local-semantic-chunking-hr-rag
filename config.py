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

    # Semantic Chunker Settings (Small Chunk: ~500 - 1.200 chars / 128 - 256 tokens)
    semantic_breakpoint_threshold: float = 0.40  # Percentile / cosine breakpoint threshold
    semantic_min_chunk_size: int = 400           # Minimum characters per chunk

    # Fixed Size Chunker Settings (Small Chunk: ~500 - 1.200 chars / 128 - 256 tokens)
    fixed_chunk_size: int = 800                  # Character/token length
    fixed_chunk_overlap: int = 150               # Overlap length

    # Sentence Chunker Settings (Sentence Level: ~100 - 250 chars / 30 - 70 tokens)
    sentence_batch_size: int = 3                 # Sentences per chunk
    sentence_overlap: int = 1                    # Sentence overlap

    # Paragraph Chunker Settings (Medium Chunk: ~1.200 - 2.500 chars / 256 - 512 tokens)
    paragraph_min_chars: int = 300               # Minimum paragraph character length
    paragraph_max_chars: int = 2000              # Maximum paragraph character length

    # Evaluation Settings
    top_k_values: List[int] = (3, 5, 10)
    data_dir: str = os.path.join(os.path.dirname(__file__), "data")
    reports_dir: str = os.path.join(os.path.dirname(__file__), "reports")

config = Config()
