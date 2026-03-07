import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    res = []
    x = np.asarray(x, dtype='float')
    res = np.where(x >= 0, x, alpha * x)

    return res