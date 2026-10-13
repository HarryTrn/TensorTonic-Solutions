"""
 *     author:  _Shinomiyaa_
 *     created: 13.10.2026 18:34:07
"""
import numpy as np

def matrix_factorization_sgd_step(U: list, V: list, r: float, lr: float, reg: float) -> list:
    """
    Returns the updated user and item vectors in a two-item list.
    """
    # Write code here
    U = np.array(U)
    V = np.array(V)
    r = np.array(r)
    e = r - np.dot(U, V.T)
    U_update = U + lr * (e * V - reg * U)
    V_update = V + lr * (e * U - reg * V)
    return [U_update.tolist(), V_update.tolist()]
    pass