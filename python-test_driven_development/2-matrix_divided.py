#!/usr/bin/python3

def matrix_divided(matrix, div):

    """
    Divides a matrix by a float or integer

    Raises errors if all the rows in the matrix aren't the same size
    If div is 0 or not a number
    If matrix has non-numbers

    Returns a new matrix that is the result of the division.
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) pf ""integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])    
