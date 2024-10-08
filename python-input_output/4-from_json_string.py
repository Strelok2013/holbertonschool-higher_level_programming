#!/usr/bin/python3
"""Module that defines the function
   from_json_string
"""
import json


def from_json_string(my_str):
    """
    Returns a string from a json string
    """
    return json.loads(my_str)
