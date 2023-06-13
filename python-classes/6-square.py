#!/usr/bin/python3

""" Defines a new square """


class Square:
    """ Initializes a square
        Args:
            size (int): size of the new square
            position (tuple): position of the square
     """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) is not tuple or len(position) != 2 \
                or type(position[0]) is not int \
                or type(position[1]) is not int \
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
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
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
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
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """ Method that calculates the area of a square object  """
    def area(self):
        return self.__size * self.__size

    """ Method that prints in stdout the square with the character # """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for k in range(0, self.__position[1]):
                    print()
            for i in range(0, self.__size):
                if self.__position[0] > 0:
                    for k in range(0, self.__position[0]):
                        print(" ", end="")
                for j in range(0, self.__size):
                    if j != self.__size - 1:
                        print("#", end="")
                    else:
                        print("#")
