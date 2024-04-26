#!/usr/bin/python3
"""
Module For Rectangle Inheriting from Base
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle Class Inheriting From Base Class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor For Rectangle Class
        Args:
            width (int): Width
            height (int): Height
            x (int, optional): x-pos. Defaults to 0.
            y (int, optional): y-pos. Defaults to 0.
            id (int, optional): Unique ID For Each Instance. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.y = y
        self.x = x

    def __str__(self) -> str:
        """
        String Representation For Instances
        Returns:
            str: String Representation For Instances
        """
        return f"[{self.__class__.__name__}] ({self.id})\
 {self.x}/{self.y} - {self.width}/{self.height}"

    @property
    def width(self):
        """
        Getter Method For Width Priv attr
        Returns:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, width: int):
        """
        Setter Method For Width Priv attr
        Args:
            width (int): Width
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if not width > 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self) -> int:
        """
        Getter Method For Height Priv attr
        Returns:
            int: Height
        """
        return self.__height

    @height.setter
    def height(self, height: int):
        """
        Setter Method For height Priv attr
        Args:
            height (int): Height
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if not height > 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def y(self) -> int:
        """
        Getter Method For y Priv attr
        Returns:
            int: y-pos
        """
        return self.__y

    @y.setter
    def y(self, y: int):
        """
        Setter Method For y Priv attr
        Args:
            y (int): y-pos
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if not y >= 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def x(self) -> int:
        """
        Getter Method For x Priv attr
        Returns:
            int: x-pos
        """
        return self.__x

    @x.setter
    def x(self, x: int):
        """
        Setter Method For x Priv attr
        Args:
            x (int): x-pos
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if not x >= 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    def area(self) -> int:
        """
        Computes Area Of Rectangle
        Returns:
            int: Area
        """
        return self.height * self.width

    def display(self):
        """
        Displays Rectangle Instance Using '#' Character
        """
        for i in range(self.y):
            print('')
        for i in range(self.height):
            for x in range(self.x):
                print(end=' ')
            for j in range(self.width):
                print('#', end='')
            print('')

    def update(self, *args, **kwargs):
        """
        Updates Attributes Of Instance
        """
        attribute_order = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                setattr(self, attribute_order[i], arg)
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
                width=self.width, height=self.height))
