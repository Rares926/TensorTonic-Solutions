import numpy as np 

def average_pooling_2d(X, pool_size):
    """
    Apply 2D average pooling with non-overlapping windows.
    """
    # Write code here
    x = np.asarray(X)
    pool_size = int(pool_size)

    if pool_size < 1:
        raise ValueError("pool_size must be greater than 1")
    
    max_w = int(x.shape[0] // pool_size)
    max_h = int(x.shape[1] // pool_size)

    out = np.zeros((max_w, max_h), dtype=float)

    for i in range(0, max_w):
        for j in range(0, max_h):
            out[i,j] = x[i*pool_size:i*pool_size+pool_size,j*pool_size:j*pool_size+pool_size].mean()
    
    return out.tolist()