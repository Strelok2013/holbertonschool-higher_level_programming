#!/usr/bin/python3
"""Defines an integer addition function?"""


def add_integer(a, b=98):
    """Returns the products of two integers or floats

    Casts floats to ints

    Raises exception when not float or int???
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
