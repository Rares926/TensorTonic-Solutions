import numpy as np

def sobel_edges(image):
    """
    Apply the Sobel operator to detect edges.
    """
    # Write code here

    kernel_sobel_1 = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    kernel_sobel_2 = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

    image = np.asarray(image)
    kernel_sobel_1 = np.asarray(kernel_sobel_1, dtype=float)
    kernel_sobel_2 = np.asarray(kernel_sobel_2, dtype=float)

    out_image = np.zeros_like(image, dtype=float)
    padd_H = kernel_sobel_1.shape[0] // 2
    padd_W = kernel_sobel_1.shape[1] // 2

    padded_image = np.zeros((
        image.shape[0] + padd_H*2,
        image.shape[1] + padd_W*2
    ))

    padded_image[
        padd_H: image.shape[0] + padd_H,
        padd_W: image.shape[1] + padd_W
    ] = image

    for i in range(out_image.shape[0]):
        for j in range(out_image.shape[1]):
            region  = padded_image[
                    i: i + kernel_sobel_1.shape[0],
                    j: j + kernel_sobel_1.shape[1]
                ]
            G_x = (region * kernel_sobel_1).sum()
            G_y = (region * kernel_sobel_2).sum()

            out_image[i,j] = np.sqrt(G_x**2+G_y**2)

    return out_image.tolist()
        