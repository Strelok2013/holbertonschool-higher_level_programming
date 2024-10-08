#!/usr/bin/python3
"""
Defines a class Square
"""


class Square:
    """
    Square
    """
    def __init__(self, size=0):
        """
        Initializes a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the area of the instance
        """
        return self.__size * self.__size
