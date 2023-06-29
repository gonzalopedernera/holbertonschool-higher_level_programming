#!/usr/bin/python3
"""Importing Base class"""


from models.base import Base
"""New class Rectangle inheriting from Base"""


class Rectangle(Base):
    """Initializes a Rectangle
    Args:
        width: width of new object
        height: height of new object
        x: x of new object
        y: y of new object
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y

    """Getter for width"""
    @property
    def width(self):
        return self.__width

    """Setter for width
    Args:
        width: new width
    """
    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    """Getter for height"""
    @property
    def height(self):
        return self.__height

    """Setter for height
    Args:
        height: new height
    """
    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    """Getter for x"""
    @property
    def x(self):
        return self.__x

    """Setter for x
    Args:
        x: new x
    """
    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    """Getter for y"""
    @property
    def y(self):
        return self.__y

    """Setter for y
    Args:
        y: new y
    """
    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    """Returns the area of a rectangle object"""
    def area(self):
        return self.__width * self.__height
