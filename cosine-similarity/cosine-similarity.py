import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    
    a = np.asarray(a)
    b = np.asarray(b)

    upper = a @ b 
    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)

    if a_norm == 0.0 or b_norm == 0.0:
        return 0.0 

    lower = a_norm * b_norm

    return upper/lower
