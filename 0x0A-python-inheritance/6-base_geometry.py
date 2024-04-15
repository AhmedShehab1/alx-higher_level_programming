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
