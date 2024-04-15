#!/usr/bin/python3
"""Module That Contains Classes And SubClasses For Geometry"""


class BaseGeometry():
    """
    Base Geometry Class (Parent)
    """

    def area(self):
        """
        Method To Calculate Area (Not Implemented)
        Raises:
            Exception: When Called
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method To Validate value
        Args:
            name (str): Name Associated With The Provided Value
            value (int): Value For a Specfic thing (ex. Distance, Age, etc.)

        Raises:
            TypeError: If value Is Not Of Type int
            ValueError: If value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if not value > 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Class Rectangle That Inherits From BaseGeometry Class
    Args:
        BaseGeometry (Class): Class That Rectangle Inherited From
    """
    def __init__(self, width, height):
        """
        Constructor For Rectangle Class
        Args:
            width (int): Width Of Rectangle
            height (int): Height of Rectangle
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        String Representation Of Instance
        Returns:
            str: String Representation
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """
        Overriding Method To Calculate Area  Of Rectangle
        Returns:
            int: Area Of Rectangle
        """
        return self.__height * self.__width


class Square(Rectangle):
    """
    Square Class That Inherits From Rectangle
    Args:
        Rectangle (Class): Class Inherited From
    """

    def __init__(self, size):
        """
        Constructor Of Square Class
        Args:
            size (int): Size Of Square
        """
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        String Representation Of Instance
        Returns:
            str: String Representation
        """
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """
        Method That Calculates Area Of Square
        Returns:
            int: Area Of Square
        """
        return self.__size ** 2
