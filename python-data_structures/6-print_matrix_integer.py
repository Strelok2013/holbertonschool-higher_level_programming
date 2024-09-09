#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # if matrix not supplied, print empty
    for i in matrix:
        for j in i:
            print("{}".format(j), end="")
        print("")
