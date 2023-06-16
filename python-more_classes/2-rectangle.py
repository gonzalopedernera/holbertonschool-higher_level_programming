#!/usr/bin/python3
""" Class for rectangle """


class Rectangle:
    """ Initializes a rectangle
        Args:
            width (int): width of the new rectangle
            height (int): height of the new rectangle
     """
    def __init__(self, width=0, height=0):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    """ Retrieves the value of width """
    @property
    def width(self):
        return self.__width

    """ Sets the value of width
        Args:
            value (int): New value for self.__width
    """
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ Retrtieves the value of height """
    @property
    def height(self):
        return self.__height

    """ Sets the value of height
        Args:
            value (int): New value for self.__height
    """
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ Returns the area of a rectangle object """
    def area(self):
        return self.__width * self.__height

    """ Return the perimeter of a rectangle object """
    def perimeter(self):
        return (self.__width + self.__height) * 2
