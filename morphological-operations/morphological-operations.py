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
    # padded_image[
    #     1:image.shape[0]+kernel.shape[0] // 2,
    #     1:image.shape[1]+kernel.shape[1] // 2
    #     ] = image

    padded_image[
        pad_h:pad_h + image.shape[0],
        pad_w:pad_w + image.shape[1]
    ] = image

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            mul = padded_image[i:i+kernel.shape[0],j:j+kernel.shape[1]] * kernel
            new_val = mul.sum()
            if operation == "dilate":
                if new_val >= 1:
                    out_image[i,j] = 1
                else:
                    out_image[i,j] = 0
            else:
                if new_val >= kernel.sum():
                    out_image[i,j] = 1
                else:
                    out_image[i,j] = 0


    return out_image.tolist()