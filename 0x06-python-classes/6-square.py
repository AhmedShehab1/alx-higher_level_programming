#!/usr/bin/python3
"""
Module to define the square class
"""


class Square:
    """
    Class Square that defines a square
    """

    def __init__(self, size=0, position=(0, 0)):
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
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integer")
        if len(position) > 2 or len(position) < 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        if not isinstance(position[0], int)or not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integer")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = position

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

    def my_print(self):
        """
        Prints To STDOUT The Square with char: "#"
        """
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(end=' ')
            for i in range(self.__size):
                print('#', end='')
            print()
        if self.__size == 0:
            for i in range(self.__position[0]):
                print(end=' ')
            print()

    @property
    def position(self) -> tuple:
        """
        Returns Current Position
        Returns:
            tuple: (x, y)
        """
        return self.__position

    @position.setter
    def position(self, value: tuple):
        """
        Modify Position Of Square
        Args:
            value (tuple): New Square Position
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integer")
        if len(value) > 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value
        self.__position = value
