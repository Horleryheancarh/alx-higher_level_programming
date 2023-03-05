#!/usr/bin/python3
"""
Module that converts an json to object
"""
import json


def from_json_string(my_obj):
    """
    Function that converts an json to object

    Args:
        my_obj: object

    Raises:
        Exception: when the object can't be decoded
    """
    return json.loads(my_obj)
