#!/usr/bin/python3
"""
Module to define the square class
"""


class Square:
    """
    Class Square that defines a square
    """

    def __init__(self, size=0):
        """
        Initializes private attribute size for current instance
        Args:
            size (int): size of square, Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns Current Square Area
        Returns:
            Area: Area Of Current Square
        """        
        return self.__size ** 2

    @property
    def size(self) -> int:
        """
        Returns The Size 
        Returns:
            int: Size of Square
        """        
        return self.__size

    @size.setter
    def size(self, value: int):
        """
        Modify Value of Size
        Args:
            value (int): New Value Of Size

        Raises:
            TypeError: When Argument Passed Not int
            ValueError: When size < 0
        """        
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
