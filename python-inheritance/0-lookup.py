#!/usr/bin/python3
"gets all the available attributes and methods of an object"


def lookup(obj):
    """Returns a list with available attributes and methods of an object
    Args:
        object: an object
    """
    return list(dir(obj))
