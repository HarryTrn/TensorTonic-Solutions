"""
 *     author:  _Shinomiyaa_
 *     created: 14.10.2026 19:18:42
"""
import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    variance = float(np.var(x, ddof=1, dtype=np.float64))
    std_dev = float(np.std(x, ddof=1, dtype=np.float64))
    return {"variance": variance, "standard_deviation": std_dev}
