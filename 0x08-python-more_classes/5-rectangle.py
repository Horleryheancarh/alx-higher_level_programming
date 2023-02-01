#!/usr/bin/python3
"""
Defines a Rectangle Class
"""


class Rectangle:
    """
    Represents a Rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Method to init instance

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Method that returns the width

        Returns:
            width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Method that defines the width

        Args:
            value: width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Method that returns the height

        Returns:
            height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Method that defines the height

        Args:
            value: heoght

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Method that returns the area

        Returns:
            area of the rectangle
        """

        return self.width * self.height

    def perimeter(self):
        """
        Method that returns the perimeter

        Returns:
            perimeter of the rectangle
        """

        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Method that prints the rectangle with #

        Returns:
            str of the rectangle
        """

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return 0

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """
        Method that returns the string rep of the instance

        Returns:
            string representation of instance
        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
        Method that prints a message when the instance is deleted
        """

        print("Bye rectangle...")
