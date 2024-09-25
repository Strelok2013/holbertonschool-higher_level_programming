#!/usr/bin/python3

"""Module that defines a function for checking objects"""


def is_same_class(obj, a_class):
    """Function that checks whether a given object
       is the same exact class, excluding inheritance
       Returns true if object is the exact class
       Returns false otherwise
    """
    if type(obj) is a_class:
        return True
    return False
