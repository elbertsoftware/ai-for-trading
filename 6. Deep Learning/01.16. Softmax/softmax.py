import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(score_list):
    exp_list = np.exp(score_list)
    return np.divide(exp_list, exp_list.sum())