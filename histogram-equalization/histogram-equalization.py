import numpy as np

def histogram_equalize(image):
    """
    Apply histogram equalization to enhance image contrast.
    """
    image = np.asarray(image)
    image_out = np.zeros_like(image)

    freq_hist = np.zeros(256)

    # compute histogram
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            freq_hist[image[i,j]] += 1

    # compute cumulative distribution function
    # my code
    # cdf = np.zeros(256)
    # cdf[0] = freq_hist[0]
    # for i in range(1,len(cdf)):
    #     cdf[i] = cdf[i-1] + freq_hist[i]

    cdf = np.cumsum(freq_hist)

    # find first non zero value for the cdf
    # cdf_min = None
    # for cdf_vl in cdf:
    #     if cdf_vl > 0 and cdf_min==None:
    #         cdf_min = cdf_vl

    # cdf_min = 0 if cdf_min is None else cdf_min

    positive = cdf[cdf > 0]
    cdf_min = positive[0] if positive.size > 0 else 0

    for i in range(image_out.shape[0]):
        for j in range(image_out.shape[1]):

            upper = cdf[image[i, j]] - cdf_min
            lower = cdf.max() - cdf_min + 1e-9

            image_out[i,j] = round((upper / lower) * 255)

    return image_out.tolist()