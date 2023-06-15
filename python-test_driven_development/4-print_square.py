#!/usr/bin/python3
""" prints a square with the character # """


def print_square(size):
    """ prints a square with the character #
    Args:
        size: size of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            if j != size - 1:
                print("#", end="")
            else:
                print("#")
