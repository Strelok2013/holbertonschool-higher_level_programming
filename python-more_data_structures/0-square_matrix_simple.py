#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    count = 0
    newMatrix = []
    for i in matrix:
        newMatrix.append(list(map(lambda x: x ** 2, i)))
        count + 1
    return newMatrix
