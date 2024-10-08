#!/usr/bin/python3
import sys
import pickle
""""""


class CustomObject():
    """"""
    name = ""
    age = 0
    is_student = False

    def __init__(self, name, age, is_student) -> None:
        self.name = name
        self.age = age
        self.is_student = is_student
        pass

    def display(self):
        """"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))
        
    def serialize(self, filename):
        """"""
        if not filename:
            print("Invalid filename")
            sys.exit()

        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except FileNotFoundError:
            print("File not found")

    @classmethod
    def deserialize(cls, filename):
        """"""
        if not filename:
            print("Invalid filename")
            sys.exit()
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("File not found")
        
        return None
