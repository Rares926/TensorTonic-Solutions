import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    pred = np.asarray(y_pred)
    target = np.asarray(y_true)

    if pred.shape != target.shape:
        return None
    
    N = len(pred)

    return (1/N)*np.sum((pred-target)**2)