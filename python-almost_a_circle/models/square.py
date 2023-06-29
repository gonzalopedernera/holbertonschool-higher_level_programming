#!/usr/bin/python3
"""Importing Rectangle class"""
from models.rectangle import Rectangle
"""New class Square inheriting from Rectangle"""


class Square(Rectangle):
    """Initializes a new Square object
    Args:
        size: size of the square
        x: x of new object
        y: y of new ovject
        id: id of new object
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Implementation of __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id,
                self.x,
                self.y,
                self.width,
                )

    """Getter for size"""
    @property
    def size(self):
        return self.width

    """Setter for size
    Args:
        size: new size
    """
    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("width must be an integer")
        self.width = size
        self.height = size
