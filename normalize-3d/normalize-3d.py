import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v = np.asarray(v)
    
    axis = 0 if v.ndim==1 else 1

    norm_value = np.sqrt(np.sum(v**2, axis=axis, keepdims=True))

    normalized_array = v/norm_value

    return np.nan_to_num(normalized_array, copy=False)