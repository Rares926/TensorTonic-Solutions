import numpy as np

def bptt_single_step(dh_next: np.ndarray, h_t: np.ndarray, h_prev: np.ndarray,
                     x_t: np.ndarray, W_hh: np.ndarray) -> tuple:
    """
    Backprop through one RNN time step.
    Returns (dh_prev, dW_hh).
    """
    # YOUR CODE HERE
    h_t = np.asarray(h_t)
    dh_next = np.asarray(dh_next)

    local_deriv = 1 - h_t**2
    d_tanh = local_deriv * dh_next

    dWhh =  d_tanh.T @ h_prev
    dhprev = d_tanh @ W_hh

    return (dhprev, dWhh)