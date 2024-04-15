#!/usr/bin/python3
"""
Module To Check For Instance's Class Inheritance
"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an
    instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.

    Args:
        obj (object): Instance Of A Class
        a_class (Class): Class To Check Wether The Object
        The instance's Class is inherited Directly Or Indirectly From it

    Returns:
        Boolean: True if the object is an instance of a class that inherited
                 (directly or indirectly) from the specified class
                 ; otherwise False
    """
    if issubclass(obj.__class__, a_class) and not (type(obj) is a_class):
        return True
    return False
