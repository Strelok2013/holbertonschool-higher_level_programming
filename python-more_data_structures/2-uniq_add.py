#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    uniq = set()
    for item in my_list:
            uniq.add(item)
    for number in uniq:
        result += number
    return result
