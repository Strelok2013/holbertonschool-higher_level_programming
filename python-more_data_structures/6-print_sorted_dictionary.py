#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    s_dictionary = sorted(a_dictionary)
    for item in s_dictionary:
        print("{}: {}".format(item, a_dictionary[item]))
