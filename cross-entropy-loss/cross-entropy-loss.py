import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """

    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    if y_true.shape[0] != y_pred.shape[0]:
        raise Exception("y_true and y_pred must have matching first dimension N")

    true_preds_probs = y_pred[np.arange(len(y_true)), y_true]

    return np.mean(-np.log(true_preds_probs))