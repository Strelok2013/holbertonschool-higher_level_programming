#!/usr/bin/python3

""""""


def write_file(filename="", text=""):
    """"""
    with open(filename, 'w', encoding="utf-8") as f:
        chars = f.write(text)
    return chars

print(write_file("written_file.txt", "text written lol"))