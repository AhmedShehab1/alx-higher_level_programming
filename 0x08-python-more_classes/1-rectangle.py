#!/usr/bin/python3
"""
Module For Rectangle
"""


class Rectangle:
    """
    class That Defines a rectangle
    """
    def __init__(self, width=0, height=0) -> None:
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def width(self) -> int:
        """
        property to retrieve the width
        Returns:
            int: Width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        property to set the value of width
        Args:
            value (int): width of rectangle

        Raises:
            TypeError: If value passed not of type int
            ValueError: If width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self) -> int:
        """
        property to retrieve the height
        Returns:
            int: height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        property to set the value of height
        Args:
            value (int): height of rectangle

        Raises:
            TypeError: If value passed not of type int
            ValueError: If height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
