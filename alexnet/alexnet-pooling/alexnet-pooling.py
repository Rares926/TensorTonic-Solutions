import numpy as np

def max_pool2d(x: np.ndarray, kernel_size: int = 3, stride: int = 2) -> np.ndarray:
    """Apply 2D max pooling (shape simulation)."""
    # YOUR CODE HERE
    
    B, img_H, img_W, features = x.shape

    out_H = (img_H - kernel_size) // stride + 1
    out_W = (img_W - kernel_size) // stride + 1

    return np.zeros((B, out_H, out_W, features))