#!/usr/bin/python3
def lookup(obj):
    """
    Function to return list of attributes and methods of an object

    Args:
        obj: instance of class

    Returns:
        Lists of attributes
    """

    return dir(obj)
