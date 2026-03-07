def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    res = []

    for point in x:

        if point > 0:

            res.append(point)

        else:

            res.append(alpha * (math.exp(point) - 1))

    return res