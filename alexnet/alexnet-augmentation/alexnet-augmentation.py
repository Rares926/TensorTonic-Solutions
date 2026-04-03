import numpy as np
import random 

def random_horizontal_flip(image: np.ndarray, p: float = 0.5) -> np.ndarray:
    """Randomly flip image horizontally."""
    # YOUR CODE HERE
    image = np.asarray(image)
    if random.random() < p:
        return image[:, ::-1, :] 
        # return np.flip(image, axis=1)
        # return np.fliplr(image)


def random_crop(image: np.ndarray, crop_size: int = 224) -> np.ndarray:
    """Extract a random crop from the image."""
    # YOUR CODE HERE
    image = np.asarray(image)
    # extract random 224 patches fgrom the 256 images 
    tl_range_H = image.shape[0] - crop_size 
    tl_range_W = image.shape[1] - crop_size

    # pick random numbers for top left values
    # option 1 
    tl_y = random.choice(range(tl_range_H))
    tl_x = random.choice(range(tl_range_W))
    # option 2
    # tl_y = random.randint(0, tl_range_H)
    # tl_x = random.randint(0, tl_range_W)

    br_y = tl_y + crop_size
    br_x = tl_x + crop_size

    return image[
        tl_y : br_y,
        tl_x : br_x
        ]
