"""
 *     author:  _Shinomiyaa_
 *     created: 13.10.2026 18:30:13
"""
def user_based_cf_prediction(similarities: list, ratings: list) -> float:
    """
    Returns the positive-similarity weighted rating prediction.
    """
    # Write code here
    numerator = sum(s * r for s, r in zip(similarities, ratings) if s > 0)
    denominator = sum(abs(s) for s in similarities if s > 0)
    return numerator / denominator if denominator else 0
    pass