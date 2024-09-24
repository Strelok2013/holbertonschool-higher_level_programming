#!/usr/bin/python3
"""Defines a module that defines the a subclass of Rectangle, Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class definition for Square, derived from Rectangle"""
    def __init__(self, size):
        """Initializes the square with size
           Runs validation check on size
           which in turn raises its own exceptions   
        """
        self.integer_validator("size", size)
        self.__width = size
        self.__height = size

    def area(self):
        """Returns the area of the Square"""
        return self.__width ** 2
