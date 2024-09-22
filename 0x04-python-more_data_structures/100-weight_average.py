#!/usr/bin/python3
"""
Additional Tasks
"""


def weight_average(my_list=[]):
    """
    Function to get the weighted avg of all integers tuple
    """
    if my_list:
        numerator = list(map(lambda x: x[0] * x[1], my_list))
        numerator = sum(numerator)
        denominator = 0
        for i in my_list:
            denominator += i[1]
        return numerator / denominator
    return 0
