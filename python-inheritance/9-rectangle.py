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
        self.integer_validator("width", width)

        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """ Returns the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
