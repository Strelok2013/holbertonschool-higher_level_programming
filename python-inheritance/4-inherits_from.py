#!/usr/bin/python3

"""Defines a module that checks if a given object
   is a derived class
"""

def inherits_from(obj, a_class):
    """Defines a function that checks whether an object is
       a sublcass
       Returns true if the object is a subclass
       Returns false otherwise
    """
    if issubclass(obj, a_class):
        return True
    return False
