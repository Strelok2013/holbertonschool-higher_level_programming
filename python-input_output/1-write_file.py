#!/usr/bin/python3

"""Module that defines the write_file function"""


def write_file(filename="", text=""):
    """Writes a specified string to a file
       with specified filename
    """
    with open(filename, 'w', encoding="utf-8") as f:
        chars = f.write(text)
    return chars
