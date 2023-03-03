#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Function that checks if obj is a type of a_class

    Args:
        obj: object
        a_class: class type

    Returns:
        True or False
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
