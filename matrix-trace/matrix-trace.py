import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    
    A = np.asarray(A)

    trace = 0.0

    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if i==j:
                trace += A[i,j]

    return trace