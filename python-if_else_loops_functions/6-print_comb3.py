#!/usr/bin/python3
for i in range(9):
    for j in range(1 + i, 10):
        print("{}".format(i), end="")
        if i != 8:
            print("{}".format(j), end=", ")
        else:
            print("{}".format(j))
