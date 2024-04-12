#!/usr/bin/python3
"""
Module That Works On Squares
"""


def print_square(size: int):
    """
    Prints Square with Character '#'
    Args:
        size (int): Size Of Square

    Raises:
        TypeError: If size is not of type int
        ValueError: if size is -ve number
    """
    if size is None or type(size) is not int:
        raise TypeError("size must be an integer")
    if not size >= 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print(end="\n" if i != size - 1 else '')
