"""
 *     author:  _Shinomiyaa_
 *     created: 12.10.2026 13:35:07
"""
def popularity_ranking(items: list, min_votes: int, global_mean: float) -> list:
    """
    Returns the weighted rating for every item.
    """
    # Write code here
    ans = []
    m = min_votes
    C = global_mean
    for i in items:
        R,v = i
        ans.append((v/(v+m))*R + (m/(v+m))*C)
    return ans
    pass