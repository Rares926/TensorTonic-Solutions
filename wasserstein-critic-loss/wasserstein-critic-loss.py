import numpy as np

def wasserstein_critic_loss(real_scores, fake_scores):
    """
    Compute Wasserstein Critic Loss for WGAN.
    """
    # Write code here
    real = np.asarray(real_scores)
    fake = np.asarray(fake_scores)

    wcl = np.mean(fake) - np.mean(real)

    return float(wcl)