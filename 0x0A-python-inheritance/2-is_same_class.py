#!/usr/bin/python3
"""Module Documentation"""


def is_same_class(obj, a_class):
    """
    Function to check if an object is an instance of a class

    Args:
        obj: object
        a_class: class type

    Returns:
        True or False
    """
    return type(obj) is a_class
