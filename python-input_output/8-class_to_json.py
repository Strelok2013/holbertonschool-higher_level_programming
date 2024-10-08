#!/usr/bin/python3
"""Module that defines the
   class_to_json function
"""


def class_to_json(obj):
    """Returns a dictionary
       representation of a given object
    """
    return obj.__dict__
