import numpy as np

def local_response_normalization(x: np.ndarray, k: float = 2, n: int = 5,
                                  alpha: float = 1e-4, beta: float = 0.75) -> np.ndarray:
    """Apply Local Response Normalization across channels."""
    # YOUR CODE HERE
    x = np.asarray(x)
    x_normed = np.zeros_like(x)

    B, H, W , ch = x.shape

    for img_id in range(B):
        for i in range(H):
            for j in range(W):
                for ch_idx in range(ch):
                    norm_val = (k + alpha * np.sum(
                        x[img_id,i,j,max(0,ch_idx-n//2):min(ch_idx+n//2,ch-1)+1]**2))**beta
                    x_normed[img_id,i,j,ch_idx] = x[img_id,i,j,ch_idx] / norm_val

    return x_normed