#!/usr/bin/python3
"""Module that contains class Rectangle"""
from models.base import Base

class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize instance"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width Getter"""
        return self.__width

    @property
    def height(self):
        """Height Getter"""
        return self.__height

    @property
    def x(self):
        """x Getter"""
        return self.__x

    @property
    def y(self):
        """y Getter"""
        return self.__y

    @width.setter
    def width(self, value):
        """Width Setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Height Setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """x Setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """y Setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """Displays a rectangle"""
        rectangle = self.y * '\n'
        for i in range(self.height):
            rectangle += (' ' * self.x)
            rectangle += ('#' * self.width) + '\n'

        print(rectangle, end='')

    def __str__(self):
        """STR special method"""
        str_rect = '[Rectangle] '
        str_id = '({}) '.format(self.id)
        str_xy = '{}/{} - '.format(self.x, self.y)
        str_wh = '{}/{}'.format(self.width, self.height)

        return str_rect + str_id + str_xy + str_wh

    def update(self, *args, **kwargs):
        """Update method"""
        if args is not None and len(args) != 0:
            lst = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, lst[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Dictionary with properties"""
        lst = ['id', 'width', 'height', 'x', 'y']
        dct = {}

        for key in lst:
            dct[key] = getattr(self, key)

        return dct
