#!/usr/bin/python3
"""Creates an Object from a “JSON file”"""


import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”
    Args:
        filename: JSON file
    """
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
