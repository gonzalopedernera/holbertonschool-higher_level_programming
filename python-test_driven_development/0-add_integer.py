#!/usr/bin/python3
def add_integer(a, b=98):
    """ Adds two digits and converts the result to ints
    Args:
        a: a number
        b: a number

    Returns:
        Addition of a and b converted to an int
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
