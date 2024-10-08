#!/usr/bin/python3
import sys
"""Module that loads and adds items
   to a json file.
   If the file does not exist,
   it creates the file.
"""

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    

try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []
items.extend(sys.argv[1:])
save_to_json_file(items, "add_item.json")