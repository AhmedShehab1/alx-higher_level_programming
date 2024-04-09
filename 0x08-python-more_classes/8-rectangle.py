#!/usr/bin/python3
"""
Module For Rectangle
"""


class Rectangle:
    """
    class That Defines a Rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

    def __repr__(self) -> str:
        """
        String Representation of Instance for Object Recreation
        Returns:
            str: String Representation of Instance
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __str__(self) -> str:
        """
        Prints String Representation of The Rectangle
        Returns:
            str: String Representation
        """
        if self.__height != 0 and self.__width != 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    print(self.print_symbol, end='')
                if i != self.__height - 1:
                    print()
        return ""

    def __del__(self):
        """
        Prints Appropriate Message Upon deletion of an instance(Rectangle)
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    def area(self) -> int:
        """
        Calculate The Area
        Returns:
            int: Area of Rectangle
        """
        return self.__width * self.__height

    def perimeter(self) -> int:
        """
        Calculates  The Perimeter of Rectangle
        Returns:
            int: Perimeter of Rectangle
        """
        return 0 if self.__width == 0 or self.__height == 0\
            else (2 * self.__height) + (2 * self.__width)

    @staticmethod
    def bigger_or_equal(rect1, rect2):
        if not isinstance(rect1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect1 if rect1.area() >= rect2.area() else rect2
