#!/usr/bin/python3
"""
Defines a class Square
"""

class Square:

    """
    Square
    """

    __size = 0

    def __init__(self, size=0):
        """
        Initializes the square
        """
        self.size = size 

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size * self.__size
    
    @property    
    def size(self):
        """
        Gets the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value