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

    def to_json(self, attrs=None):
        """Returns a dictionary representation
           of the class including only the
           specified attributes.
        """
        if (type(attrs) is list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Reconstructs a student class from
           a json file.
        """
        for key, value in json.items():
            setattr(self, key, value)