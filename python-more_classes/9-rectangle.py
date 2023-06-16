#!/usr/bin/python3
""" Class for rectangle """


class Rectangle:
    """ Initializes a rectangle
        Args:
            width (int): width of the new rectangle
            height (int): height of the new rectangle
     """
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    """ Method that prints in stdout the rectangle with the character # """
    def __str__(self):
        hashtangle = ""
        if self.__width == 0 or self.__height == 0:
            return hashtangle
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                hashtangle += str(self.print_symbol)
            if i != self.__height - 1:
                hashtangle += "\n"
        return hashtangle

    """ Return a string representation of the rectangle """
    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    """ Prints 'Bye rectangle...' when a rectangle is deleted """
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    """ Returns the biggest rectangle based on the area
        Args:
            rect_1: object of class Rectangle
            rect_2: object of class Rectangle
    """
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 > area_2 or area_1 == area_2:
            return rect_1
        elif area_2 > area_1:
            return rect_2

    """ Returns a new Rectangle instance with width == height == size
        Args:
            size (int): value to asign the width and height of new object
    """
    @classmethod
    def square(cls, size=0):
        return cls(size, size)
