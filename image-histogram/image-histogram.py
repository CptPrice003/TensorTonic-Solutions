def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    hist = [0] * 256

    for i in range(len(image)):

        for j in range(len(image[i])):

            hist[image[i][j]] += 1

    return hist

    