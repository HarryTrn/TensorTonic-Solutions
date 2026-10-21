"""
 *     author:  _Shinomiyaa_
 *     created: 21.10.2026 10:56:17
"""
import math
import numpy as np
def cosine_embedding_loss(x1: list, x2: list, label: int, margin: float) -> float:
    """
    Returns the cosine embedding loss as a float.
    """
    # Write code here
    x1 = np.asarray(x1)
    x2 = np.asarray(x2)    
    cosine_similarity = np.dot(x1, x2) / (np.linalg.norm(x1) * np.linalg.norm(x2))

    loss = float(1 - cosine_similarity) if label == 1 else float(max(0, cosine_similarity - margin))
    return loss