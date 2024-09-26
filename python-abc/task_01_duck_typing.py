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

    def __init__(self, radius):
        """"""
        self.__radius = radius

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