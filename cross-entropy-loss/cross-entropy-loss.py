"""
 *     author:  _Shinomiyaa_
 *     created: 13.10.2026 10:25:00
"""
import numpy as np

def cross_entropy_loss(y_true: list[int], y_pred: list[list[float]]) -> float:
    """
    Returns the mean multiclass cross-entropy loss as a Python float.
    """
    # Write code here
    if len(y_true) != len(y_pred):
        return None 
    else:
        return -1/len(y_true) * np.sum(np.log(np.array([y_pred[i][y_true[i]] for i in range(len(y_true))])))
    pass