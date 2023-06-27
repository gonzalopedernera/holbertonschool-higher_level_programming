#!/usr/bin/python3
"""New class Base"""


class Base:
    __nb_objects = 0

    """New object initialization
    Args:
        id: new object id
    """
    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
