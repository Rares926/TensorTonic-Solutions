def gaussian_fc(x, y, sigma):
    return np.exp(
        -(x**2+y**2)/(2*(sigma**2))
    )

import numpy as np 

def gaussian_kernel(size, sigma):
    """
    Generate a normalized 2D Gaussian blur kernel.
    """
    # Write code here
    kernel = np.zeros((size,size))
    kernel_center = (size // 2, size //2)

    all_val_sum = 0.0
    for i in range(size):
        for j in range(size):
            offset_x = j-kernel_center[1]
            offset_y = i-kernel_center[0]
            kernel[i,j] = gaussian_fc(offset_x, offset_y, sigma)
            all_val_sum += kernel[i,j]
    
    kernel = kernel/all_val_sum
    return kernel.tolist()