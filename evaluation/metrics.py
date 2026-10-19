from typing import List
from baselines.base import Chunk

def chunk_contains_snippet(chunk_content: str, snippet: str) -> bool:
    """
    Checks if a chunk contains a ground truth snippet (case-insensitive and whitespace normalized).
    Also supports token overlap matching for slightly varied phrasings.
    """
    c_norm = " ".join(chunk_content.lower().split())
    s_norm = " ".join(snippet.lower().split())

    # Exact substring match
    if s_norm in c_norm:
        return True

    # High token-level overlap match (>= 80% of keywords present in chunk)
    s_tokens = set(s_norm.split())
    if len(s_tokens) == 0:
        return False
    c_tokens = set(c_norm.split())
    overlap = len(s_tokens.intersection(c_tokens))
    return (overlap / len(s_tokens)) >= 0.8

def evaluate_retrieval_for_query(
    retrieved_chunks: List[Chunk],
    ground_truth_snippets: List[str],
    top_k_list: List[int] = (3, 5, 10)
) -> dict:
    """
    Evaluates retrieval performance for a single query against its ground truth snippets.
    Returns Recall@K for each K and Reciprocal Rank (RR).
    """
    if not ground_truth_snippets:
        return {"rr": 0.0, **{f"recall@{k}": 0.0 for k in top_k_list}}

    results = {}
    total_snippets = len(ground_truth_snippets)

    # 1. Reciprocal Rank (MRR component)
    first_hit_rank = 0
    for rank, chunk in enumerate(retrieved_chunks, start=1):
        if any(chunk_contains_snippet(chunk.content, snippet) for snippet in ground_truth_snippets):
            first_hit_rank = rank
            break

    results["rr"] = 1.0 / first_hit_rank if first_hit_rank > 0 else 0.0

    # 2. Recall@K
    for k in top_k_list:
        top_k_chunks = retrieved_chunks[:k]
        hits = 0
        for snippet in ground_truth_snippets:
            if any(chunk_contains_snippet(chunk.content, snippet) for chunk in top_k_chunks):
                hits += 1
        results[f"recall@{k}"] = hits / total_snippets

    return results
