#!/usr/bin/python3
"""
Module that converts an object to json
"""
import json


def to_json_string(my_obj):
    """
    Function that converts an object to json

    Args:
        my_obj: object

    Raises:
        Exception: when the object can't be encoded
    """
    return json.dumps(my_obj)
