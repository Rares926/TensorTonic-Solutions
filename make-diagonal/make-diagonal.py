import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    
    out = np.zeros((len(v), len(v)))

    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            if i==j:
                out[i,j] = v[i]

    return out