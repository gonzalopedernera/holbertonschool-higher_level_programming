#!/usr/bin/python3
"""Importing JSON module"""
import json

"""New class Base"""


class Base:

    """New object initialization
    Args:
        id: new object id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries
        Args:
            list_directories: a list of dictionaries
        """
        return json.dumps(list_dictionaries)
