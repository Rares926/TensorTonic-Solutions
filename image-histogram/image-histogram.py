import numpy as np

def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here

    image = np.asarray(image)

    histo = np.zeros(256)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            histo[image[i][j]] += 1

    return histo.tolist()
