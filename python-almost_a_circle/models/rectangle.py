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

    def area(self):
        """Return the area of a rectangle object"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        if self.__y > 0:
            for i in range(0, self.__y):
                print()
        for i in range(0, self.__height):
            if self.__x > 0:
                for k in range(0, self.__x):
                    print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Impletementation of __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id,
                self.__x,
                self.__y,
                self.__width,
                self.__height
        )

    def update(self, *args, **kwargs):
        """Updates a Rectangle object attributes
        Args:
            *args: argument vector
            **kwargs: argument vector with key/value format
        """
        arg = list(args)
        if len(arg) >= 1:
            self.id = arg[0]
            if len(arg) >= 2:
                self.__width = arg[1]
            if len(arg) >= 3:
                self.__height = arg[2]
            if len(arg) >= 4:
                self.__x = arg[3]
            if len(arg) >= 5:
                self.__y = arg[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value
