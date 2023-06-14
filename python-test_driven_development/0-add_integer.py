#!/usr/bin/python3
""" Adds two numbers and converts the result to int """


def add_integer(a, b=98):
    """ Adds two numbers and converts the result to int
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
