#!/usr/bin/python3
"""
Module that writes an object to a file in json format
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an object to a file in json format

    Args:
        my_obj: object
        filename: filename

    Raises:
        Exception: when the object can't be encoded
    """

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
