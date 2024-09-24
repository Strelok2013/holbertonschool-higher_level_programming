#!/usr/bin/python3

"""Defines a module for the base geometry class"""


class BaseGeometry:
    """Defines the BaseGeometry class"""
    def area(self):
        """Raises an exception if this method is used on the base class
           or an undefined method within a subclass
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks whether or not a given value is an integer value over 0
           Raises a Type error if the value is non-integer
           Raises a Value error if the value is less than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        
        if value < 0:
            raise ValueError("{} must be greater than 0".format(name))
