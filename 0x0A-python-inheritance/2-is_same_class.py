#!/usr/bin/python3
"""
Module To Check If The Provided Instance Is
exactly an instance of a particular class
"""


def is_same_class(obj, a_class):
    """
    Function That returns True if the object is exactly an
    instance of the specified class ; otherwise False.
    Args:
       obj (Object): Instance Of A Class
       a_class (Class): Class To Check Wether The
       Provided Instance's Class is exactly the same

    Returns:
       Boolean: True if the object is exactly an
       instance of the specified class ; otherwise False.
    """
    if type(obj) is a_class:
        return True
    return False
