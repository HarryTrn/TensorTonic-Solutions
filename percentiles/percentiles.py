"""
 *     author:  _Shinomiyaa_
 *     created: 14.10.2026 19:22:59
"""
import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns a NumPy array of percentiles.
    """
    # Write code here
    return np.percentile(x, q)
    pass