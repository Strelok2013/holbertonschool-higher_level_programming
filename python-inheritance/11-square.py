#!/usr/bin/python3
"""Defines a module that defines the a subclass of Rectangle, Square"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class definition for Square, derived from Rectangle"""
    def __init__(self, width, height):
        """Initializes the square with size
           Runs validation check on size
           which in turn raises its own exceptions   
        """
        integer_validator(width)

        integer_validator(height)

        self.__width = width
        self.__height = height

    def area():
        """Returns the area of the Square"""
        return width ** 2

    def __str__():
        """Returns a string representation of Square"""
        return "[Square] {}/{}".format(width, height)
