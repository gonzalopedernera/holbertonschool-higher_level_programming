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

    def update(self, *args, **kwargs):
        """Updates a Square object attributes
        Args:
            *args: argument vector
            **kwargs: argument vector with key/value format
        """
        arg = list(args)
        if len(arg) >= 1:
            self.id = arg[0]
            if len(arg) >= 2:
                self.width = arg[1]
                self.height = arg[1]
            if len(arg) >= 3:
                self.x = arg[2]
            if len(arg) >= 4:
                self.y = arg[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                    self.height
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
