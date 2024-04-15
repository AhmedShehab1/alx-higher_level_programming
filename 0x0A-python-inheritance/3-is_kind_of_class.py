#!/usr/bin/python3
"""
Module To Check For Instance's Class Inheritance
"""


def is_kind_of_class(obj, a_class):
    """
     function that returns True if the object is an instance of,
     or if the object is an instance of a class that inherited from,
     the specified class ; otherwise False.

    Args:
        obj (Object): Instance Of A Class
        a_class (Class): Class To Check Wether The Provided
        Instance's Class is as or inherited from it

    Returns:
        Boolean: True if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class; otherwise False.
    """
    return isinstance(obj, a_class)
