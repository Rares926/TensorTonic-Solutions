import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    # Your code here

    v = np.asarray(v)

    if len(v.shape) == 1:
        return np.sqrt(np.sum([el**2 for el in v]))
    else:
        res = np.zeros(v.shape[0])
        for idx, vect in enumerate(v):
            res[idx] = np.sqrt(np.sum([el**2 for el in vect])).item()
        return res
