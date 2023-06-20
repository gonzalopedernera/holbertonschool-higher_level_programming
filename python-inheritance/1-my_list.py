#!/usr/bin/python3
"""New class that inherits from list"""


class MyList(list):
    """New class that inherits from list"""
    def print_sorted(self):
        """Prints a sorted version of a list"""
        sortedl = []
        sortedl = list(self)
        sortedl.sort()
        print("{}".format(sortedl))
