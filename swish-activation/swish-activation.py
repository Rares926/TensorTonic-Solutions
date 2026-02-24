import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    clipped_x = np.clip(x, -100, 100)
    sigmoid_val = (1/(1+np.exp(-clipped_x)))
    swish_val = x * sigmoid_val
    if swish_val.ndim==0:
        return np.asarray([swish_val])
    return swish_val