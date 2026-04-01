import numpy as np 


def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """

    if not isinstance(matrix, (np.ndarray, list)):
        return None

    matrix =  np.asarray(matrix)
    if matrix.ndim != 2:
        return None

    if axis not in [None, 0, 1]:
        return None
    
    eps = 1e-8

    if norm_type == "l1":
        return matrix / (np.sum(np.abs(matrix), axis=axis, keepdims=True) + eps)
    elif norm_type == "l2":
        return matrix / (np.sqrt(np.sum(matrix**2, axis=axis, keepdims=True)) + eps)
    elif norm_type == "max":
        return matrix / (np.max(np.abs(matrix), axis=axis, keepdims=True) + eps)
    else:
        return None