#!/usr/bin/python3
"""Checks if class object with inheritance"""


def is_kind_of_class(obj, a_class):
    """Returns True if object belongs to a_class with inheritance, otherwise,
    returns False
    Args:
        obj: an object
        a_class: class to check
    """
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
