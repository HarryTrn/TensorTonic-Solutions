"""
 *     author:  _Shinomiyaa_
 *     created: 14.10.2026 19:28:17
"""
import numpy as np

def chi2_independence(C: list) -> dict:
    """
    Returns a dictionary with chi2 and expected.
    """
    # Write code here
    C = np.asarray(C, dtype=np.float64)
    return {
        "chi2": float(np.sum((C - np.outer(np.sum(C, axis=1), np.sum(C, axis=0)) / np.sum(C)) ** 2 / (np.outer(np.sum(C, axis=1), np.sum(C, axis=0)) / np.sum(C)))),
        "expected": (np.outer(np.sum(C, axis=1), np.sum(C, axis=0)) / np.sum(C))
    }
    pass