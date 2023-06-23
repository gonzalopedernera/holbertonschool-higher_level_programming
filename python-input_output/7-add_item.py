#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file"""

import sys


save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file

try:
    args = load_from_json("add_item.json")
except Exception:
    args = []
if len(sys.argv) != 1:
    for i in range(1, len(sys.argv)):
        args.append(sys.argv[i])

save_to_json(args, "add_item.json")
