import numpy as np

def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    # formula 
    # Y=0.299⋅R+0.587⋅G+0.114⋅B
    R_w, G_w, B_w = 0.299, 0.587, 0.114

    image = np.asarray(image)
    image_gray = np.zeros(
        (image.shape[0], image.shape[1]), dtype=float)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            R_grey_val = image[i][j][0] * R_w
            G_grey_val = image[i][j][1] * G_w
            B_grey_val = image[i][j][2] * B_w
            image_gray[i,j] = R_grey_val + G_grey_val + B_grey_val

    return image_gray.tolist()