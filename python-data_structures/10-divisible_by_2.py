#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    divisible = []
    for item in my_list:
        if item % 2 == 0:
            divisible.append(True)
        else:
            divisible.append(False)
    return divisible
