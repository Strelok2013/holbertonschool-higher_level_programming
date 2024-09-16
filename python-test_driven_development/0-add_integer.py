#!/usr/bin/python3
"""Defines an integer addition function?"""

def add_integer(a, b=98):
    """
    Returns the products of two integers or floats

    Casts floats to ints

    Raises exception when not float or int???
    """
    try:
        if a or b is not int or float:
            raise TypeError
        if isinstance(a, float):
            int_a = int(a)
        else:
            int_a = a
        if isinstance(b, float):
            int_b = int(b)
        else:
            int_b = b
        return int_a + int_b
         
    except TypeError:
        if a is not float or int:
            print("a must be an integer")
        if b is not float or int:
            print("b must be an integer")
