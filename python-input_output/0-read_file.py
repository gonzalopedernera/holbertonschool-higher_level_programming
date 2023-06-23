#!/usr/bin/python3
"""Open a file and print its content"""


def read_file(filename=""):
    """Open a file and print its content
    Args:
        filename: name of the file to print
    """
    with open(filename, encoding="utf-8") as f:
        reading = f.read()
        print("{}".format(reading))
    f.closed
