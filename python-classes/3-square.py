#!/usr/bin/python3

""" Defines a new square """


class Square:
    """ Initializes a square
        Args:
            size (int): size of the new square
     """
    def __init__(self, size=0):
        if type(size) is not int:
            print("size must be an integer", end="")
            raise TypeError
        if size < 0:
            print("size must be >= 0", end="")
            raise ValueError

        self.__size = size

    """ Method that calculates the area of a square object  """
    def area(self):
        self.area = self.__size * self.__size
        return self.area
