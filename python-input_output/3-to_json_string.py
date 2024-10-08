#!/usr/bin/python3
"""Module that defines the function to_json_string"""
import json


def to_json_string(my_obj):
    """Returns a json string from a specified object"""
    return json.dumps(my_obj)
