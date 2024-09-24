#!/usr/bin/python3
"""Defines a module for a sublcass of BaseGeometry, Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a subclass of BaseGeometry, Rectangle"""
    def __init__(self, width, height):
        """Initializes a rectangle with width and height
           Runs validation checks on width and height
           which in turn raise exceptions if they fail
        """
        integer_validator(width)

        integer_validator(height)

        self.__width = width
        self.__height = height
