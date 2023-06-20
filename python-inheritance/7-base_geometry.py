#!/usr/bin/python3
"""New empty class"""


class BaseGeometry:
    """Function placeholder with exception message"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if value is a valid integer
        Args:
            name: name for the value
            value: an int
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
