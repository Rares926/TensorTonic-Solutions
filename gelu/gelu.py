import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: scalar, list, or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    # Write code here
    # prerequisites
    x = np.asarray(x, dtype=float)
    v_func = np.vectorize(math.erf)
    # computing
    return (1/2)*x*(1+v_func(x / np.sqrt(2)))