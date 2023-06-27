#!/usr/bin/python3
"""New class Base"""


class Base:

    """New object initialization
    Args:
        id: new object id
    """
    _nb__objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
