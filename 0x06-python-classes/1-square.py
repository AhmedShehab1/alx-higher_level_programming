#!/usr/bin/python3
"""
Module to define the square class
"""
class Square:
    """
    Class Square that defines a square
    """
    def __init__(self, size):
        """
        Initializes private attribute size for current instance

        Args:
            size (no type/value verification): size of square
        """
        self.__size = size
