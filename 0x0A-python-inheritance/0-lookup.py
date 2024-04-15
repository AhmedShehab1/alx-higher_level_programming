#!/usr/bin/python3
"""A Module To Give A Glimpse of available methods and attributes
    of an object
"""


def lookup(obj):
    """
    Returns Methods And Attributes Available For An Object
    Args:
        obj (object): Object To Be Examined

    Returns:
        list: list of available Methods And Objects
    """
    return dir(obj)
