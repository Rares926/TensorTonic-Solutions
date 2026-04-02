import numpy as np

def alexnet_conv1(image: np.ndarray) -> np.ndarray:
    """AlexNet first conv layer: 11x11, stride 4, 96 filters (shape simulation)."""
    # YOUR CODE HERE
    B, img_H, img_W, channels = image.shape
    kernel_H, kernel_W = 11, 11
    stride = 4
    filters = 96
    out_H, out_W = 55, 55

    pad_H = ((out_H-1)*stride-img_H+kernel_H)/2
    pad_W = ((out_W-1)*stride-img_W+kernel_W)/2

    return np.ones((B, out_H, out_W, filters))
