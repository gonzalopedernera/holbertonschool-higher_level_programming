#!/usr/bin/python3
"""Writes a file in Json"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation
    Args:
        my_obj: object to convert to JSON
        filename: name of the file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
