import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here

    x = np.asarray(x, dtype=float)
    max_val = np.maximum(0, x)
    if len(max_val.shape)==0:
        return np.asarray(max_val, dtype=float)
    return max_val