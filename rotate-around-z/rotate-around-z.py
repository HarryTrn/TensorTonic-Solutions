"""
 *     author:  _Shinomiyaa_
 *     created: 20.10.2026 10:18:48
"""
import numpy as np

def rotate_around_z(points: list, theta: float) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as points.
    """
    # Write code here
    values = np.asarray(points)
    consine = np.cos(theta)
    sine = np.sin(theta)
    x = values[..., 0] * consine - values[..., 1] * sine
    y = values[..., 0] * sine + values[..., 1] * consine
    z = values[..., 2]
    return np.stack((x, y, z), axis=-1)
