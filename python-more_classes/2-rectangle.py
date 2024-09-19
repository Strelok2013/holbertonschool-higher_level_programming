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
        Getter/Setter for Width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter/Setter for  Height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        Returns 0 if either width or height are equal to 0
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)
