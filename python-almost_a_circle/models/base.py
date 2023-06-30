#!/usr/bin/python3
"""Importing JSON module"""
import json
import os.path
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
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = []
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

    """Returns an instance with all attributes already set
    Args:
        **dictionary: attributes for new object
    """
    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2, 3, 4, 156)
        if cls.__name__ == "Square":
            dummy = cls(2, 3, 4, 156)

        dummy.update(**dictionary)

        return dummy

    """Returns a list of instances from a <Class name>.json file"""
    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json'

        if os.path.isfile('./' + filename):
            with open(filename, 'r', encoding="utf-8") as f:
                obj_dict = cls.from_json_string(f.read())
                obj_list = []
                for i in obj_dict:
                    obj = cls.create(**i)
                    obj_list.append(obj)
                return obj_list
        else:
            return []
