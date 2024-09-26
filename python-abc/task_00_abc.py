#!/usr/bin/python3
""""""
from abc import ABC
from abc import abstractmethod


class Animal(ABC):
    """"""
    @abstractmethod
    def sound():
        pass

class Dog(Animal):
    """"""
    def sound():
        return "Bark"
    
class Cat(Animal):
    """"""
    def sound():
        return "Meow"