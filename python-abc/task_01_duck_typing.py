#!/usr/bin/python3
""""""

from abc import ABC
from abc import abstractmethod
import math


class Shape(ABC):
    """"""
    @abstractmethod
    def area():
        """"""
        pass

    @abstractmethod
    def perimeter():
        """"""
        pass

class Circle(Shape):
    """"""

    def __init__(self, radius=0):
        """"""
        if radius < 0:
            raise ValueError("Radius must be greater than 0")
        self.__radius = radius

    @property
    def radius(self):
        """"""
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        """"""
        if value < 0:
            value = abs(value)
        
        self.__radius = value

    def area(self):
        """"""
        return math.pi * self.__radius ** 2

    def perimeter(self):
        """"""
        return 2 * math.pi * self.__radius

class Rectangle(Shape):
    """"""
    def __init__(self, width, height):
        """"""
        self.__width = width
        self.__height = height

    def area(self):
        """"""
        return self.__width * self.__height

    def perimeter(self):
        """"""
        return (self.__width * 2) + (self.__height * 2)

def shape_info(shape):
    """"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

shape_info(circle)
shape_info(rectangle)