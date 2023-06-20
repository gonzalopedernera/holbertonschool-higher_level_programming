#!/usr/bin/python3
"""Gets class of an object without inheritance"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance of the specified class
    ; otherwise False
    Args:
        obj: an object
        a_class: class to check
    """
    if type(obj) == a_class:
        return True
    else:
        return False
