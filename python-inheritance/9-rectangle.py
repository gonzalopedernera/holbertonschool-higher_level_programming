#!/usr/bin/python3
"""Import BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Initialization of a new class object
    Args:
        width (int): width of the new Rectangle
        height (int): height of the new Rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    """Return the area of a Rectangle object"""
    def area(self):
        return self.__height * self.__width

    """str implementation"""
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
