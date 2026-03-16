import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    y = np.asarray(y_train)
    X = np.asarray(X_test)

    clases, frequency = np.unique(y, return_counts=True)
    max_idx = np.argmax(frequency)

    return np.full_like(X, clases[max_idx])