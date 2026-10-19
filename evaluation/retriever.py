import re
import math
import requests
from typing import List, Tuple
from baselines.base import Chunk
from baselines.semantic_chunker import check_ollama_alive
from config import config

class InMemVectorRetriever:
    """
    In-memory vector retrieval engine for benchmarking.
    Computes dense vector representations via local Ollama embedding model
    (or graceful deterministic fallback), and performs Cosine Similarity search.
    """
    def __init__(self, ollama_url: str = config.ollama_base_url, model_name: str = config.embedding_model):
        self.ollama_url = ollama_url.rstrip("/")
        self.model_name = model_name
        self.indexed_chunks: List[Chunk] = []
        self.embeddings: List[List[float]] = []

    def _get_ollama_embedding(self, text: str) -> List[float]:
        if check_ollama_alive(self.ollama_url):
            try:
                resp = requests.post(
                    f"{self.ollama_url}/api/embeddings",
                    json={"model": self.model_name, "prompt": text},
                    timeout=config.embedding_timeout
                )
                if resp.status_code == 200:
                    data = resp.json()
                    return data.get("embedding", [])
            except Exception:
                pass
        return self._fallback_embedding(text)

    def _get_ollama_batch_embeddings(self, texts: List[str]) -> List[List[float]]:
        if check_ollama_alive(self.ollama_url):
            try:
                resp = requests.post(
                    f"{self.ollama_url}/api/embed",
                    json={"model": self.model_name, "input": texts},
                    timeout=config.embedding_timeout
                )
                if resp.status_code == 200:
                    data = resp.json()
                    if "embeddings" in data and len(data["embeddings"]) == len(texts):
                        return data["embeddings"]
            except Exception:
                pass
            return [self._get_ollama_embedding(t) for t in texts]
        return [self._fallback_embedding(t) for t in texts]

    def _fallback_embedding(self, text: str) -> List[float]:
        words = re.findall(r'\w+', text.lower())
        dim = 256
        vec = [0.0] * dim
        for w in words:
            h = hash(w) % dim
            vec[h] += 1.0
        norm = math.sqrt(sum(v * v for v in vec))
        if norm > 0:
            vec = [v / norm for v in vec]
        return vec

    def _cosine_similarity(self, vec_a: List[float], vec_b: List[float]) -> float:
        dot = sum(a * b for a, b in zip(vec_a, vec_b))
        norm_a = math.sqrt(sum(a * a for a in vec_a))
        norm_b = math.sqrt(sum(b * b for b in vec_b))
        if norm_a == 0 or norm_b == 0:
            return 0.0
        return dot / (norm_a * norm_b)

    def index_chunks(self, chunks: List[Chunk]):
        self.indexed_chunks = chunks
        if not chunks:
            self.embeddings = []
            return

        texts = [c.content for c in chunks]
        self.embeddings = self._get_ollama_batch_embeddings(texts)

    def search(self, query: str, top_k: int = 5, filter_doc_id: str = None) -> List[Tuple[Chunk, float]]:
        if not self.indexed_chunks:
            return []

        query_vec = self._get_ollama_embedding(query)
        scored: List[Tuple[Chunk, float]] = []

        for chunk, emb in zip(self.indexed_chunks, self.embeddings):
            if filter_doc_id and chunk.doc_id != filter_doc_id:
                continue
            sim = self._cosine_similarity(query_vec, emb)
            scored.append((chunk, sim))

        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_k]
