#!/usr/bin/python3
import json
"""Module that defines the function 
   from_json_string
"""


def from_json_string(my_str):
    """
    Returns a string from a json string
    """
    return json.loads(my_str)
