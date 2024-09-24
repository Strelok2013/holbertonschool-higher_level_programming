#!/bin/usr/python3

"""Defines a module for the base geometry class"""

class BaseGeometry():
    """Defines the BaseGeometry class"""
    def area(self):
        """Raises an exception if this method is used on the base class
           or an undefined method within a subclass
        """
        raise Exception("area() is not implemented")
