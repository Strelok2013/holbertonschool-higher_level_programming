#!/usr/bin/python3

class Square:
    __size = 0

    def __init__(self, size):
        self.__size = size 

    def area(self):
        return self.__size * self.__size
    
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value

    def my_print(self):
        for i in range(0, self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print("")