"""
 *     author:  _Shinomiyaa_
 *     created: 21.10.2026 10:47:19
"""
import numpy as np

def contrastive_loss(a: list, b: list, y: list, margin: float = 1.0, reduction: str = "mean") -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    a = np.asarray(a,dtype=np.float64)
    b = np.asarray(b,dtype=np.float64)
    y = np.asarray(y,dtype=np.float64)
    if np.ndim(a) == 1: a = a.reshape(1, -1)
    if np.ndim(b) == 1: b = b.reshape(1, -1)
    d = np.linalg.norm(a - b, axis=1)
    loss = float((y * d**2 + (1 - y) * (np.maximum(0, margin - d))**2).mean()) if reduction == "mean" else float((y * d**2 + (1 - y) * (np.maximum(0, margin - d))**2).sum())
    return loss