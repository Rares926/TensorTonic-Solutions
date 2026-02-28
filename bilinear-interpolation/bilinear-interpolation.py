import numpy as np
import math

def bilinear_resize(image, new_h, new_w):
    """
    Resize a 2D grid using bilinear interpolation.
    """
    # Write code here
    epsilon = 1e-10

    image = np.asarray(image)
    img_H = image.shape[0]
    img_W = image.shape[1]
    output_image = np.zeros((new_h, new_w))
    for i in range(new_h):
        for j in range(new_w):

            src_y = i * ((img_H-1)/(new_h-1 + epsilon))
            src_x = j * ((img_W-1)/(new_w-1 + epsilon))

            y0 = math.floor(src_y)
            x0 = math.floor(src_x)

            dy = math.modf(src_y)[0]
            dx = math.modf(src_x)[0]

            y1 = min(y0+1, img_H-1)
            x1 = min(x0+1, img_W-1)

            top_left = image[y0,x0]*(1-dy)*(1-dx)
            top_right = image[y1,x0]*dy*(1-dx)
            bottom_right = image[y0,x1]*(1-dy)*dx
            bottom_left = image[y1,x1]*dy*dx

            output_image[i,j] = top_left + top_right + bottom_right + bottom_left

    return output_image.tolist()
