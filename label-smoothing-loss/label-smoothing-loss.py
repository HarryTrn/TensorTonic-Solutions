"""
 *     author:  _Shinomiyaa_
 *     created: 13.10.2026 10:12:08
"""

import math

def label_smoothing_loss(predictions: list, target: int, epsilon: float) -> float:
    """
    Returns cross-entropy loss for the smoothed target distribution.
    """
    # Write code here
    arr = [(1-epsilon) + epsilon/len(predictions) if i == target else epsilon/len(predictions) for i in range(len(predictions))]
    return -sum([arr[i] * math.log(predictions[i]) for i in range(len(predictions))])
print(label_smoothing_loss([0.1, 0.2, 0.7], 2, 0.1))