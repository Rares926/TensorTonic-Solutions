import numpy as np

def rotate_image(image, angle_degrees):
    """
    Rotate the image counterclockwise by the given angle using nearest neighbor interpolation.
    """
    # Write code here

    image = np.asarray(image)
    angle_degrees = int(angle_degrees)
    angle_rad = np.deg2rad(angle_degrees)
    cx = (image.shape[1]-1)/2
    cy = (image.shape[0]-1)/2

    image_rotated = np.zeros_like(image)
    for i_y in range(image.shape[0]):
        for j_x in range(image.shape[1]):
            
            dx = j_x - cx
            dy = i_y - cy

            src_x = round(cx - dy * np.sin(angle_rad) + dx * np.cos(angle_rad))
            src_y = round(cy + dy * np.cos(angle_rad) + dx * np.sin(angle_rad))

            # out shape is already filled with zero if we have out of bound pixels 
            # we simply do nothing
            if 0 <= src_x < image.shape[1] and 0 <= src_y < image.shape[0]:
                image_rotated[i_y, j_x] = image[src_y, src_x]
                            
    return image_rotated.tolist()