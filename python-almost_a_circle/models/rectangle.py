#!/usr/bin/python3
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
        self.width = width
        self.height = height
        self.x = x
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
        self.__y = y
