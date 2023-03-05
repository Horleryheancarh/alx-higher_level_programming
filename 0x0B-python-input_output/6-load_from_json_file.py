#!/usr/bin/python3
"""
Module that creates an object from a json file
"""
import json


def load_from_json_file(filename):
    """
    Function that creates an object from a json file

    Args:
        filename: filename

    Raises:
        Exception: when the object can't be encoded
    """

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
