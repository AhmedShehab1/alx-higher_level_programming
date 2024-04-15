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
