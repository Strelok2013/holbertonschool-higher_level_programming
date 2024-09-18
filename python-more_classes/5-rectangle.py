#!/usr/bin/python3

"""

"""

class Rectangle:
    """
    
    """
    def __init__(self, width=0, height=0):
        """
        
        """
        self.__width = width
        self.__height = height

    @property
    
    def width(self):
        """
        
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
        
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        
        rect = []

        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height -1:
                rect.append("\n")
        return "".join(rect)
    
    def __repr__(self):
        """
        
        """
        rect = "Rectange(" + str(self.__Width)
        rect += "," + str(self.__height) + ")"
        return rect
    
    def __del__(self):
        """
        
        """
        print("Bye rectangle...")