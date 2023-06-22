#!/usr/bin/python3
"""Import Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square object initialization
        Args:
            size(int): size of the square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    """Return the area of a square object"""
    def area(self):
        return self.__size * self.__size

    """str impletentation"""
    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
