#!/usr/bin/python3

"""
    Defines a function that formats text
"""

def text_indentation(text):
    """
        Splits a string into lines based on delimiters
        Raises an exception if input isn't a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    c = 0 
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
