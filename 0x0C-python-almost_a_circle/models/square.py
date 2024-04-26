#!/usr/bin/python3
"""
Module For Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square Class Inheriting From Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor For Square Objects
        Args:
            size (int) : Size
            x (int, optional): x-pos. Defaults to 0.
            y (int, optional): y-pos. Defaults to 0.
            id (int, optional): Unique ID For Each Instance. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Public Getter For Size Of Square
        Returns:
            int: Size Of Square
        """
        return self.width

    @size.setter
    def size(self, size: int):
        """
        Setter For Square Size
        Args:
            size (int): Size Of Square
        """
        self.width = size
        self.height = size

    def __str__(self) -> str:
        """
        String Representation For Instances
        Returns:
            str: String Representation For Instances
        """
        return f"[{self.__class__.__name__}] ({self.id})\
 {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs) -> None:
        """
        Updates Attributes Of Instance
        """
        attr_order = ['id', 'size', 'x', 'y']
        if args:
            for index, arg in enumerate(args):
                setattr(self, attr_order[index], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Provides instance's attributes
        as a dictionary
        Returns:
            dict: Dictionary Containing
            All Instance's Attribute along
            with their current values
        """
        return (dict(id=self.id, x=self.x, y=self.y,
                size=self.width))
