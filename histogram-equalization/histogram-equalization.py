import numpy as np

def histogram_equalize(image):
    """
    Apply histogram equalization to enhance image contrast.
    """
    image = np.asarray(image)
    max_pix = image.max() + 1

    freq_hist = np.zeros(max_pix) # frequency histogram

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            freq_hist[image[i,j]] += 1

    cdf = np.zeros(max_pix)
    cdf[0] = freq_hist[0]
    for i in range(1,len(cdf)):
        cdf[i] = cdf[i-1] + freq_hist[i]

    image_out = np.zeros_like(image)

    cdf_min = None
    for cdf_vl in cdf:
        if cdf_vl > 0 and cdf_min==None:
            cdf_min = cdf_vl

    if cdf_min==None:
        cdf_min = 0

    for i in range(image_out.shape[0]):
        for j in range(image_out.shape[1]):

            upper = cdf[image[i,j]]-cdf_min
            lower = cdf.max()-cdf_min

            if lower == 0.0:
                image_out[i,j] = 0.0
                continue

            image_out[i,j] = round((upper /lower) * 255)


    return image_out.tolist()