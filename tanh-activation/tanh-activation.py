import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    
    x = np.asarray(x, dtype=float)
    upper = np.exp(x) - np.exp(-x)
    lower = np.exp(x) + np.exp(-x)
    
    tanh_val = upper/lower

    if tanh_val.ndim == 0:
        return np.asarray([tanh_val])
    
    return tanh_val