#!/usr/bin/python3

"""Module that defines the read_file function"""


def read_file(filename=""):
    """reads a file using the specified name
        and prints it out
    """
    with open(filename, encoding="utf-8") as f:
        data = f.read()
    print(data)
