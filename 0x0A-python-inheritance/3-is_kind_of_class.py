#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Function that checks if obj is an instance of a_class

    Args:
        obj: object
        a_class: class type

    Returns:
        True or False
    """
    return isinstance(obj, a_class)
