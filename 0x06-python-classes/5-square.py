#!/usr/bin/python3
class Square:
    """Class to define square
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
        """Method to reutrn area of the square
        """
        return self.__size ** 2

    @property
    """Method to return size of the square
    """
    def size(self):
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

    def my_print(self):
        """Method to print the square with #
        """
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
