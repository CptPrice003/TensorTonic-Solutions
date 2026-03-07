import numpy as np

def selu(x, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    """
    Apply SELU activation element-wise.
    Returns a list of floats rounded to 4 decimal places.
    """
    res = []

    for p in x:

        if p > 0:

            res.append(round(lam * p, 4))

        else:

            res.append(round(lam * alpha * (math.exp(p) - 1),4))

    return res