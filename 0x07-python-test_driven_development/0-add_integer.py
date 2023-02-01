#!/usr/bin/python3
"""A function that adds two numbers"""


def add_integer(a, b=98):
    """
    Args:
        a: integer or float
        b: integer or float

    Returns:
        Sum of the inputs

    Raises:
        TypeError: If a or b are not integer or float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
