"""
 *     author:  _Shinomiyaa_
 *     created: 14.10.2026 11:26:53
"""
import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    # Write code here
    return (np.array(X) - np.mean(X, axis=axis, keepdims=True)) / (np.where(np.std(X, axis=axis, keepdims=True) > eps, np.std(X, axis=axis, keepdims=True), 1.0))
    pass