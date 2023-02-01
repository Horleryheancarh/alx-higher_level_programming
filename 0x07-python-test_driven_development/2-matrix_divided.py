#!/usr/bin/python3
"""
Divide the numbers of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all the elements of a matrix

    Args:
        matrix: list of lists of integers/floats
        div: number which divides the matrix

    Returns:
        A new matrix with the results

    Raises:
        TypeError:
            If the elements of matrix aren't lists
            If the elements aren't integers/floats
            If div is not an integer/float
            If the lists of the matrix do not have the same size
        ZeroDivisionError:
            If div is zero
    """
    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    length = 0
    msg_size = "Each row of the matrix must have the same size"

    if (len(matrix) == 0):
        raise TypeError(msg_type)

    for elems in matrix:
        if (not elems) or (not isinstance(elems, list)):
            raise TypeError(msg_type)

        if length != 0 and len(elems) != length:
            raise TypeError(msg_size)

        for i in elems:
            if not type(i) in (int, float):
                raise TypeError(msg_type)

        length = len(elems)

    an = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return an
