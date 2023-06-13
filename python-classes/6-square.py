#!/usr/bin/python3

""" Defines a new square """


class Square:
    """ Initializes a square
        Args:
            size (int): size of the new square
            position (tuple): position of the square
     """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    """ Retrieves the positioning of the square """
    @property
    def position(self):
        return self.__position

    """ Method to set the position of the square
        Args:
            value (int): value to set the square's position to
    """
    @position.setter
    def postion(self, value):
        if type(position) is not tuple or position[0] < 0 or position[1] < 0:
            print("position must be a tuple of 2 positive integers")
            raise TypeError
        self.__position = value

    """ Method that calculates the area of a square object  """
    def area(self):
        return self.__size * self.__size

    """ Method that prints in stdout the square with the character # """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    if j != self.__size - 1:
                        print("#", end="")
                    else:
                        print("#")