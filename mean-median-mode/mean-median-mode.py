import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """

    x = np.asarray(x)
    
    return(
        np.mean(x),
        np.median(x),
        list(Counter(x))[0]
    )