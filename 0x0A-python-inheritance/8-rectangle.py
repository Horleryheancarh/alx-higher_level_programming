#!/usr/bin/python3
"""Module Documentation"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class that defines Recatngle from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initializes instance
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
