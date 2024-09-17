#!/usr/bin/python3

"""
    Defines a function that prints a square
"""

def print_square(size):

    """
    Prints a square of a given size
    Raises an exception when a negative number is used or a non-integer is used
    Prints nothing on a 0-sized square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >=0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if size == 0:
        print("")
    if size == 1:
        print("#")

    for i in range(size):
        print("#" * size)
