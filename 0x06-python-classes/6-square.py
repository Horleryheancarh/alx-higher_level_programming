#!/usr/bin/python3
class Square:
    """Class to define square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Method to initialize square
        """
        self.__size = int(size)
        self.__position = position

    def area(self):
        """Method to return area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Method to return size of the square
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

    @property
    def position(self):
        """Method to return position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Method to set position in the square
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive numbers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive numbers')
        if not isinstance(value[0], int):
            raise TypeError('position must be a tuple of 2 positive numbers')
        if not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive numbers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive numbers')
        self.__position = value

    def my_print(self):
        """Method to print square with #
        """
        if not self.__size:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()
