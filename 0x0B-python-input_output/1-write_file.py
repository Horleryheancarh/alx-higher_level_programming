#!/usr/bin/python3
"""
Module that writes to text file
"""


def write_file(filename="", text=""):
    """
    Function that writs to a file

    Args:
        filename: filename
        text: text to write

    Raises:
        Exception: when the file can't be opened
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
