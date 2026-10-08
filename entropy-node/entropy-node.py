"""
 *     author:  _Shinomiyaa_
 *     created: 08.10.2026 10:54:57
"""
import numpy as np

def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    # Write code here
    cnt = np.unique(y, return_counts=True)
    return -np.sum((cnt[1] / len(y)) * np.log2(cnt[1] / len(y)))
    pass