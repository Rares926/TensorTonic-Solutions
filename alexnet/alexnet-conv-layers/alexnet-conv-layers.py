import numpy as np

def alexnet_conv1(image: np.ndarray) -> np.ndarray:
    """AlexNet first conv layer: 11x11, stride 4, 96 filters (shape simulation)."""
    # YOUR CODE HERE
    B, img_H, img_W, channels = image.shape
    kernel_H, kernel_W = 11, 11
    stride = 4
    filters = 96
    padding = 2
    
    out_H = (img_H + 2 * padding - kernel_H) // stride + 1
    out_W = (img_W + 2 * padding - kernel_W) // stride + 1
    
    return np.zeros((B, out_H, out_W, filters))
