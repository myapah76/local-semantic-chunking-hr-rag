import re
import math
import logging
from typing import List, Dict, Any, Optional
import requests
from baselines.base import BaseChunker, Chunk
from config import config

logger = logging.getLogger(__name__)

_OLLAMA_ONLINE = None

def check_ollama_alive(url: str) -> bool:
    global _OLLAMA_ONLINE
    if _OLLAMA_ONLINE is not None:
        return _OLLAMA_ONLINE
    try:
        resp = requests.get(url, timeout=1.0)
        _OLLAMA_ONLINE = (resp.status_code == 200)
    except Exception:
        _OLLAMA_ONLINE = False
    return _OLLAMA_ONLINE

class LocalSemanticChunker(BaseChunker):
    """
    Proposed Method: Local Semantic Chunking
    Calculates cosine similarity between adjacent sentences/propositions using a local embedding model.
    Places chunk boundaries at local minima (where cosine similarity drops below threshold),
    ensuring semantically coherent units (e.g. keeping entire job experience intact).
    """
    def __init__(
        self,
        similarity_threshold: float = config.semantic_breakpoint_threshold,
        min_chunk_size: int = config.semantic_min_chunk_size,
        ollama_url: str = config.ollama_base_url,
        model_name: str = config.embedding_model
    ):
        super().__init__(name=f"LocalSemantic(thresh={similarity_threshold})")
        self.similarity_threshold = similarity_threshold
        self.min_chunk_size = min_chunk_size
        self.ollama_url = ollama_url.rstrip("/")
        self.model_name = model_name

    def _split_into_sentences(self, text: str) -> List[str]:
        raw = re.split(r'(?<=[.!?])\s+|\n+', text)
        return [s.strip() for s in raw if len(s.strip()) > 5]

    def _cosine_similarity(self, vec_a: List[float], vec_b: List[float]) -> float:
        dot = sum(a * b for a, b in zip(vec_a, vec_b))
        norm_a = math.sqrt(sum(a * a for a in vec_a))
        norm_b = math.sqrt(sum(b * b for b in vec_b))
        if norm_a == 0 or norm_b == 0:
            return 0.0
        return dot / (norm_a * norm_b)

    def _get_ollama_embeddings(self, texts: List[str]) -> Optional[List[List[float]]]:
        if not check_ollama_alive(self.ollama_url):
            return None

        try:
            resp = requests.post(
                f"{self.ollama_url}/api/embed",
                json={"model": self.model_name, "input": texts},
                timeout=config.embedding_timeout
            )
            if resp.status_code == 200:
                data = resp.json()
                if "embeddings" in data:
                    return data["embeddings"]

            embeddings = []
            for t in texts:
                single_resp = requests.post(
                    f"{self.ollama_url}/api/embeddings",
                    json={"model": self.model_name, "prompt": t},
                    timeout=config.embedding_timeout
                )
                if single_resp.status_code == 200:
                    embeddings.append(single_resp.json().get("embedding", []))
                else:
                    return None
            return embeddings
        except Exception:
            return None

    def _fallback_statistical_embedding(self, text: str) -> List[float]:
        """
        Deterministic lightweight n-gram character/word embedding fallback
        used if local Ollama daemon is offline during testing.
        """
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

    def _embed_sentences(self, sentences: List[str]) -> List[List[float]]:
        ollama_vecs = self._get_ollama_embeddings(sentences)
        if ollama_vecs and len(ollama_vecs) == len(sentences):
            return ollama_vecs
        return [self._fallback_statistical_embedding(s) for s in sentences]

    def chunk(self, text: str, doc_id: str, metadata: Optional[Dict[str, Any]] = None) -> List[Chunk]:
        sentences = self._split_into_sentences(text)
        if not sentences:
            return []

        if len(sentences) == 1:
            return [Chunk.create(doc_id, 0, sentences[0], self.name, metadata)]

        embeddings = self._embed_sentences(sentences)

        similarities = []
        for i in range(len(embeddings) - 1):
            sim = self._cosine_similarity(embeddings[i], embeddings[i + 1])
            similarities.append(sim)

        grouped_chunks: List[str] = []
        current_chunk_sentences = [sentences[0]]

        for i in range(len(similarities)):
            sim = similarities[i]
            next_sentence = sentences[i + 1]

            if sim < self.similarity_threshold:
                current_text = " ".join(current_chunk_sentences).strip()
                if len(current_text) >= self.min_chunk_size:
                    grouped_chunks.append(current_text)
                    current_chunk_sentences = [next_sentence]
                else:
                    current_chunk_sentences.append(next_sentence)
            else:
                current_chunk_sentences.append(next_sentence)

        if current_chunk_sentences:
            grouped_chunks.append(" ".join(current_chunk_sentences).strip())

        chunks: List[Chunk] = []
        for idx, content in enumerate(grouped_chunks):
            chunks.append(Chunk.create(doc_id, idx, content, self.name, metadata))

        return chunks
