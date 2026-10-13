"""
 *     author:  _Shinomiyaa_
 *     created: 13.10.2026 11:01:50
"""
import math

def log_loss(y_true: list, y_pred: list, eps: float = 1e-15) -> list:
    """
    Returns a list of loss values.
    """
    # Write code here
    return [-float(y_true[i] * math.log(max(eps, min(1 - eps, y_pred[i]))) + (1 - y_true[i]) * math.log(1 - max(eps, min(1 - eps, y_pred[i])))) for i in range(len(y_true))]
    pass