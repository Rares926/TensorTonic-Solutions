import numpy as np

def absolut_substraction(x,y):
    return np.abs(x-y)

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    
    x = np.asarray(x)
    y = np.asarray(y)

    vectorized_absolut_substraction = np.vectorize(absolut_substraction)

    return float(np.sum(vectorized_absolut_substraction(x,y)))

