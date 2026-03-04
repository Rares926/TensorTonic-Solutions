import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here
    
    true = np.asarray(y_true)
    pred = np.asarray(y_pred)
    
    e = true - pred

    hl =  np.where(
        np.abs(e) <= delta,
        (1/2)*(e**2),
        delta*(np.abs(e)-(1/2)*delta)
    )

    return np.mean(hl)