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
    for i in range(image.shape[1]):
        for j in range(image.shape[0]):
            
            dx = j - cx
            dy = i - cy

            src_x = round(cx - dy * np.sin(angle_rad) + dx * np.cos(angle_rad))
            src_y = round(cy + dy * np.cos(angle_rad) + dx * np.sin(angle_rad))

            image_rotated[i ,j] = image[src_y, src_x]

    return image_rotated.tolist()