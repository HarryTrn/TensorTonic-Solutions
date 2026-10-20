"""
 *     author:  _Shinomiyaa_
 *     created: 20.10.2026 09:53:51
"""
import numpy as np

def angle_between_3d(v: list, w: list) -> float:
    """
    Returns the angle as a float.
    """
    # Write code here
    return np.arccos(np.clip(np.dot(v, w) / (np.linalg.norm(v) * np.linalg.norm(w)), -1.0, 1.0))
    pass