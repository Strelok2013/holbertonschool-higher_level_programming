#!/usr/bin/python3

"""Module that defines the append_write function"""


def append_write(filename="", text=""):
    """
    Appends a string of text to a specified file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        chars = f.write(text)
    return chars
