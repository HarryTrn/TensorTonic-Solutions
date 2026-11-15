"""
 *     author:  _Shikimori_
 *     created: 15.11.2026 07:50:39
"""
import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    # Write code here
    k = num_classes if num_classes else np.max(y) + 1
    n = len(y)
    one_hot_arr = np.zeros((n,k),dtype=int)
    for i in range(n): one_hot_arr[i,y[i]] = 1
    return one_hot_arr
    pass