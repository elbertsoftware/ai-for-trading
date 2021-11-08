import numpy as np


# As in the video, Y in the quiz is for the category, and P is the probability.
# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    return -np.sum([y * np.log(p) + (1 - y) * np.log(1 - p) for y, p in zip(Y, P)])
