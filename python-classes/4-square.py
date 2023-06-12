#!/usr/bin/python3

""" Defines a new square """


class Square:
    """ Initializes a square
        Args:
            size (int): size of the new square
     """
    def __init__(self, size=0):
        self.__size = size

    """ Retrieves the value of size """
    @property
    def size(self):
        return self.__size

    """ Sets the value of size
        Args:
            value (int):
                New value for self.__size
    """
    @size.setter
    def size(self, value):
        if type(value) is not int:
            print("size must be an integer", end="")
            raise TypeError
        if value < 0:
            print("size must be >= 0", end="")
            raise ValueError
        self.__size = value

    """ Method that calculates the area of a square object  """
    def area(self):
        return self.__size * self.__size
