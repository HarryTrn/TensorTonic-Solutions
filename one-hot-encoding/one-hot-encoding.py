"""
 *     author:  _Shinomiyaa_
 *     created: 14.10.2026 11:51:06
"""
import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    # Write code here
    K = num_classes if num_classes else max(y) + 1
    N = len(y)
    one_hot_arr = np.zeros((N, K), dtype=int)
    for i in range(N):
        one_hot_arr[i, y[i]] = 1
    return one_hot_arr
    pass