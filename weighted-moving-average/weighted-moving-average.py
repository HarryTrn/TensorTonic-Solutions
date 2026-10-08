"""
 *     author:  _Shinomiyaa_
 *     created: 08.10.2026 10:05:53
"""
import numpy as np
def weighted_moving_average(values: list, weights: list) -> list:
    """
    Returns the weighted average of every complete window.
    """
    # Write code here
    weights = np.asarray(weights)
    values = np.asarray(values)
    sum_w = float(np.sum(weights))
    res = []
    for i in range(len(values) - len(weights) + 1):
        res.append(np.sum(values[i:i + len(weights)] * weights) / sum_w)
    return res

# values = list(map(int, input().split()))
# w = list(map(int, input().split()))

# print(weighted_moving_average(values, w))