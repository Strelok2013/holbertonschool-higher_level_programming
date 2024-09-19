#!/usr/bin/python3

"""
Defines a class called Rectangle
"""


class Rectangle:
    """
        A rectangle >:|
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @classmethod
    def square(cls, size=0):
        """
        Returns a rectange with width and height equal to size
        """
        return (cls(size, size))

    @property
    def width(self):
        """
        Getter/Setter for width
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
        Getter/Setter for height
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
        Returns the area of the Rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the Rectangle
        Returns 0 if either the width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Returns a string representation of the Rectangle to be used in print()
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []

        for i in range(self.__height):
            [rect.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """
        Returns a formal string representation of the Rectangle
        """
        rect = "Rectange(" + str(self.__Width)
        rect += "," + str(self.__height) + ")"
        return rect

    def __del__(self):
        """
        Prints a message when an instance of the Rectangle is deleted
        Also decrements the number of instances
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns a rectangle which has the bigger area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError()
        if not isinstance(rect_2, Rectangle):
            raise TypeError()

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
