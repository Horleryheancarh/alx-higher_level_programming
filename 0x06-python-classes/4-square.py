#!/usr/bin/python3
"""Define a Class Square"""


class Square:
    """Class to define a square
    """
    def __init__(self, size=0):
        """Method to initialize square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = int(size)

    def area(self):
        """Method return area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Method to return size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Method to set size of the square
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = int(value)
