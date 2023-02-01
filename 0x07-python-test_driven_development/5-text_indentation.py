#!/usr/bin/python3
"""
Function to add 2 new lines after the characters .?:
"""


def text_indentation(text):
    """
    Prints 2 new lines after '.?:'

    Args:
        text: input string

    Returns:
        no return

    Raises:
        TypeError:
            If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = text[:]

    for i in ".?:":
        lst = s.split(i)
        s = ""
        for j in lst:
            j = j.strip(" ")
            s = j + i if s == "" else s + "\n\n" + j + i

    print(s[:-3], end="")
