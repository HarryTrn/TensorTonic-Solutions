"""
 *     author:  _Shinomiyaa_
 *     created: 13.10.2026 18:29:15
"""
def rating_normalization(matrix: list) -> list:
    """
    Returns the mean-centered user-item matrix.
    """
    normalized = []

    for r in matrix:
        ratings = [x for x in r if x != 0]
        if not ratings:
            normalized.append([0] * len(r))
            continue
        mean = sum(ratings) / len(ratings)
        normalized.append([x - mean if x != 0 else 0 for x in r])
    return normalized
