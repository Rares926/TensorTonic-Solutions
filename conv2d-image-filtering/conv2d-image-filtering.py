import numpy as np 

def pad2d(image, padding=0):
    """
    Pad a 2D image array
    """
    padded_image = np.zeros(
        (image.shape[0]+padding*2,
         image.shape[1]+padding*2)
         )
    padded_image[
        padding:padded_image.shape[0]-padding,
        padding:padded_image.shape[1]-padding
        ] = image
    
    return padded_image

def conv2d(image, kernel, stride=1, padding=0):
    """
    Apply 2D convolution to a single-channel image.
    """
    # Write code here
    
    image = np.asarray(image)
    kernel = np.asarray(kernel)

    padded_image = pad2d(image, padding)

    out_H = (image.shape[0]+ 2 * padding - kernel.shape[0])//stride + 1
    out_W = (image.shape[1]+ 2 * padding - kernel.shape[1])//stride + 1
    
    out = np.zeros((out_H,out_W))

    k_H, k_W = kernel.shape

    for i in range(out.shape[0]):
        for j in range(out.shape[1]):

            op_out = padded_image[
                i*stride:i*stride+k_H,
                j*stride:j*stride+k_W
                ] * kernel

            out[i,j] = op_out.sum()

    return out.tolist()