#!/usr/bin/python3
"""Module that class Square that inherits from Rectangle"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """STR special method"""
        str_s = '[Square] '
        str_id = '({}) '.format(self.id)
        str_xy = '{}/{} - '.format(self.x, self.y)
        str_ss = '{}'.format(self.size)

        return str_s + str_id + str_xy + str_ss

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update method"""
        if args is not None and len(args) != 0:
            lst = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if lst[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, lst[i], args[i])
        else:
            for k, v in kwargs.items():
                if k == 'size':
                    setattr(self, 'width', v)
                    setattr(self, 'height', v)
                else:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Dictionary with properties"""
        lst = ['id', 'width', 'height', 'x', 'y']
        dct = {}

        for key in lst:
            if key == 'size':
                dct[key] = getattr(self, 'width')
            else:
                dct[key] = getattr(self, key)

        return dct
