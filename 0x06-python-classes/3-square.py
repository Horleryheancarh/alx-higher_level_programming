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
        """Method to return area of the square
        """
        return self.__size ** 2
