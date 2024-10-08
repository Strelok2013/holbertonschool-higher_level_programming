#!/usr/bin/python3
import json
"""Module that defines the
   save_to_json_file function
"""


def save_to_json_file(my_obj, filename):
    """Saves an object to json string
       inside a json file
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
