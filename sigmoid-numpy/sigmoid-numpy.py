import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x = np.array(x, dtype=float)
    x = np.nan_to_num(x, posinf=500, neginf=500)
    return 1/(1+np.exp(-x))