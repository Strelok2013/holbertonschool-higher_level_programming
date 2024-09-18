#!/usr/bin/python3
"""
Defines a class Square
"""

class Square:
    """
    Square
    """
    __size = 0
    __position = (0, 0)

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.size = size 
        self.position = position

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size ** 2

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

    @property
    def position(self):
        """
        Gets the position of the square
        """
        return self.__position
    
    @position.setter
    def position(self, value):
        """
        Sets the position of the square
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        
    def my_print(self):
        """
        Prints the square based on its position and size
        """
        if self.__size == 0:
            print("")
            return
        
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")