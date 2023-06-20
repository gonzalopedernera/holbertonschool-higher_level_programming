#!/usr/bin/python3
"""Checks if obj belongs to a class that inherited a_class"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class inherited by a_class
    Args:
        obj: an object
        a_class: class to check
    """
    if isinstance(obj, a_class) is True and type(obj) != a_class:
        return True
    else:
        return False
