#!/usr/bin/python3

""""""


class Student():
    """"""
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, fName, lName, a) -> None:
        self.first_name = fName
        self.last_name = lName
        self.age = a
        pass

    def to_json(self):
        return self.__dict__
