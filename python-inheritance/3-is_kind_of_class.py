#!/usr/bin/python3

"""Defines a module for a function that checks 
   an instance of a class
"""

def is_kind_of_class(obj, a_class):
    """Function that checks whether an object is
       an instance of a derived class
       accounts for inheritance
       returns true if object is an instance
       returns false otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
