import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def binary_cross_entropy(preds, targets):
    
    return - np.mean(
        targets * np.log(preds) + 
        (1 - targets) * np.log(1 - preds)
        )

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    X = np.asarray(X)
    y = np.asarray(y)

    N = X.shape[0]
    # first we init the weights and bias 
    W = np.zeros(X.shape[1])
    b = np.zeros(1)

    for _ in range(steps):
        # compute predictions and apply activation
        preds = X @ W + b
        activated_preds = _sigmoid(preds)

        # compute loss
        loss_val = binary_cross_entropy(activated_preds, y)

        # compute derivatives 
        d_w = (1/N) * X.T @ (activated_preds-y)
        d_b = (1/N) * np.sum(activated_preds-y)

        # update params in the opossite direction of the gradient
        W = W - lr * d_w
        b = b - lr * d_b

    return W, b