#!/usr/bin/python3
"""
Function to print a square with #
"""


def print_square(size):
    """
    Print square with #

    Args:
        size: size of the square

    Returns:
        No return

    Raises:
        TypeError:
            If size is not an integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
