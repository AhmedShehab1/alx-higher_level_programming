#!/usr/bin/python3
"""
Module For Addition Of Integers
"""
def add_integer(a, b=98) -> int:
    """
    Function That Adds Two Integers
    Args:
        a (int or float): First operand
        b (int or float, 98): Second Operand. Defaults to 98.

    Raises:
        TypeError: If a is not of type float and int
        TypeError: If b is not of type float and int

    Returns:
        int: Sum of a and b
    """
    if type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")
    a, b = map(int, [a, b])
    return a + b
