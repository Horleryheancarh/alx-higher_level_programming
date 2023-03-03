#!/usr/bin/python3
"""Module Documentation"""


class MyInt(int):
    """
    Inherits from class int
    """

    def __eq__(self, other):
        """
        Function that returns != check
        """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """
        Function that returns == check
        """
        return int.__eq__(self, other)
