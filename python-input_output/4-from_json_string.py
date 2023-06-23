#!/usr/bin/python3
"""Import Json module"""


import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string
    Args:
        my_str: JSON string to convert
    """
    return json.loads(my_str)
