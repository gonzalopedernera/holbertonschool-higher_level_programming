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
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    """writes the JSON string representation of list_objs to a file
    Args:
        list_objs: a list of instances of base"""
    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="utf-8") as f:
            list_dict = []
            if list_objs is None:
                f.write(list_dict)
            else:
                for i in list_objs:
                    list_dict.append(i.to_dictionary())
                f.write(Base.to_json_string(list_dict))

    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string
        Args:
            json_string: a string representation of a list of directories
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
