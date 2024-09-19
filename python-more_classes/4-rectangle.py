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

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        Returns 0 if either the width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Defines how to print the Rectangle using print() or str()
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []

        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """
        Returns a formal string representation of the rectangle instance.
        """
        rect = "Rectange(" + str(self.__Width)
        rect += "," + str(self.__height) + ")"
        return rect
