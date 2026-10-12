"""
 *     author:  _Shinomiyaa_
 *     created: 12.10.2026 13:41:00
"""
def top_k_recommendations(scores: list, rated_indices: list, k: int) -> list:
    """
    Returns the highest-scoring unrated item indices.
    """
    # Write code here
    unrated_scores = [(i, scores[i]) for i in range(len(scores)) if i not in rated_indices]
    unrated_scores.sort(key=lambda x: x[1], reverse=True)
    return [i for i, _ in unrated_scores[:k]]
