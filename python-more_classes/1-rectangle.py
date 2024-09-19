#!/usr/bin/python3

"""
Defines a class called Rectangle
"""


class Rectangle:
    """
        A rectangle >:|
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter/Setter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError()
        if value < 0:
            raise ValueError()
        self.__width = value

    @property
    def height(self):
        """
        Getter/Setter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError()
        if value < 0:
            raise ValueError()
        self.__height = value
