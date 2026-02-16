import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """

    x = np.asarray(x)
    
    return(
        np.mean(x).item(),
        np.median(x).item(),
        list(Counter(x))[0]
    )