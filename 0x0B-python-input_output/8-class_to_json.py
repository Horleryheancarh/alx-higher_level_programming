#!/usr/bin/python3
"""
Module that converts a class to dictionary
"""


def class_to_json(my_obj):
    """
    Function that converts a class object to a dictionary

    Args:
        my_obj: Class Object
    """
    dit = {}

    if hasattr(my_obj, "__dict__"):
        dit = my_obj.__dict__.copy()

    return dit
