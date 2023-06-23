#!/usr/bin/python3
"""Writes a file"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the number of
    characters written
    Args:
        filename: name of the file
        text: text to write on the file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
