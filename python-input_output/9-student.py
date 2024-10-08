#!/usr/bin/python3

"""Module that defines the Student class"""


class Student():
    """Class definition for Student"""
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, fName, lName, a) -> None:
        """Initializes the student class"""
        self.first_name = fName
        self.last_name = lName
        self.age = a
        pass

    def to_json(self):
        """Returns a dictionary representation
           of the class
        """
        return self.__dict__
