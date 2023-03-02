#!/usr/bin/python3
class MyList(list):
    """
    Class that inherits the attributes ref of list

    Args:
        list: class list
    """

    def print_sorted(self):
        """
        Method that prints sorted list
        """
        sorted = self.copy()
        sorted.sort()
        print(sorted)
