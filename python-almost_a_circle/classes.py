#!/usr/bin/python3
"""Classes"""
import json

class Base:
    instances = []
    @classmethod
    def savetofile(cls, listobjs):
        with open("object_list.json", 'w', encoding="utf-8") as f:
            f.write(json.dumps(listobjs))
    

    def fromjsonstring(jsonstring):
        return list(json.loads(jsonstring))

    def loadfromfile(cls):
        return cls.instances

class Rectangle(Base):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.instances.append(self)

    @width.setter
    def width(self, width):
        self.__width = width

    @height.setter
    def height(self, height):
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def display(self):
        hashtangle = ""
        if self.__width == 0 or self.__height == 0:
            print("{}".format(hashtangle), end="")
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                hashtangle += "#"
            if i != self.__height - 1:
                hashtangle += "\n"
        print("{}".format(hashtangle))

    def __str__:
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def update(self, *args, kwargs):
        self.__width = args[0]
        self.__height = args[1]

    def to_dictionary(self):
        return dir(self)

class Square(Rectangle):

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    def to_dictionary(self):
        return dir(self)


