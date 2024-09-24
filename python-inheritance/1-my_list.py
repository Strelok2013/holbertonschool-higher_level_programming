#!/usr/bin/python3

"""Defines a module that creates a custom list class"""


class MyList(list):
    """Definition of the MyList class"""
    def print_sorted(self):
        """Prints the contents of the derived list
           Sorted in ascending order
        """
        print(sorted(self))
