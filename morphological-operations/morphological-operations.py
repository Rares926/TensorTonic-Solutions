import numpy as np

def morphological_op(image, kernel, operation):
    """
    Apply morphological erosion or dilation to a binary image.
    """
    # Write code here
    image = np.asarray(image)
    kernel = np.asarray(kernel)
    out_image = np.zeros_like(image)

    pad_h = kernel.shape[0] // 2
    pad_w = kernel.shape[1] // 2

    padded_image = np.zeros(
        (
            image.shape[0]+pad_h*2,
            image.shape[1]+pad_w*2
        )
    )

    padded_image[
        pad_h:pad_h + image.shape[0],
        pad_w:pad_w + image.shape[1]
    ] = image

    kernel_sum = kernel.sum()

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region  = padded_image[
                i: i + kernel.shape[0],
                j: j + kernel.shape[1]
            ]

            new_val = (region * kernel).sum()

            if operation == "dilate":
                out_image[i, j] = int(new_val >= 1)
            else: # "erode"
                out_image[i,j] = int(new_val >= kernel_sum)

    return out_image.tolist()