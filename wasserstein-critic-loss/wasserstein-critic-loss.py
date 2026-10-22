"""
 *     author:  _Shinomiyaa_
 *     created: 22.10.2026 11:49:06
"""
import numpy as np

def wasserstein_critic_loss(real_scores: list, fake_scores: list) -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    real_scores = np.asarray(real_scores)
    fake_scores = np.asarray(fake_scores)
    # if len(real_scores) < len(fake_scores):
    #     real_scores = np.pad(real_scores, (0, len(fake_scores) - len(real_scores)), 'constant')
    # elif len(fake_scores) < len(real_scores):
    #     fake_scores = np.pad(fake_scores, (0, len(real_scores) - len(fake_scores)), 'constant')
    # return float(np.mean(1/len(fake_scores) * np.sum(fake_scores)) - np.mean(1/len(real_scores) * np.sum(real_scores)))
    return float(np.mean(fake_scores) - np.mean(real_scores))
    pass