#!/usr/bin/python3
"""Module Documentation"""


class BaseGeometry:
    """
    Class that defines Geometric shapes attributes
    """
    def area(self):
        """
        Method that defines the area of a geometric shape
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        """

        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
