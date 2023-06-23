#!/usr/bin/python3
"""Import Json module"""


import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)
    Args:
        my_obj: object to convert
    """
    return json.dumps(my_obj)
