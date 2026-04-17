import numpy as np

def rnn_forward(X: np.ndarray, h_0: np.ndarray,
                W_xh: np.ndarray, W_hh: np.ndarray, b_h: np.ndarray) -> tuple:
    """
    Forward pass through entire sequence.
    """
    # YOUR CODE HERE
    W_xh = np.asarray(W_xh)
    W_hh = np.asarray(W_hh)
    X = np.asarray(X)
    
    B, T, input_dim = X.shape
    
    all_h = []
    h_prev = h_0
    
    for time_step in range(T):
        h_new = np.tanh(X[:,time_step,:] @ W_xh.T + h_prev @ W_hh.T + b_h)
        h_prev = h_new
        all_h.append(h_new)

    return (
        np.stack(all_h, axis=1),
        all_h[-1]
    )
