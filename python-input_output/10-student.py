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

    def to_json(self, attrs=None):
        """"""
        if (type(attrs) is list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
