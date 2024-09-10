#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq = []
    for item in my_list:
        for item2 in uniq:
            if item == item2:
                continue
            else:
                uniq.append(item)
    print(uniq)

uniq_add