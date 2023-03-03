#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class that defines Square from Recatngle class
    """

    def __init__(self, size):
        """
        Initializes instance
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        Method that  returns the area of the instance
        """
        return super().area()
