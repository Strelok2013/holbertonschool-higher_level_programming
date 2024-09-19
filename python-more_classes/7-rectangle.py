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

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the Rectangle
        Returns 0 if either width of height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Returns a string representation of the rectangle used in print()
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []

        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
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
        Prints a message when deleting a Rectangle
        Decrements the number of instances
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")