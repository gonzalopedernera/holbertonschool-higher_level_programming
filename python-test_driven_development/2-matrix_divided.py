#!/usr/bin/python3
""" Divides all elements on a matrix by a specified divisor """


def matrix_divided(matrix, div):
    """ Divides all elements on a matrix by a specified divisor
    Args:
        matrix: a matrix of floats/ints
        div: Divisor for the division

    Returns:
        a new matrix with all the results
    """
    if len(matrix) != 0:
        if type(div) not in [int, float]:
            raise TypeError("div must be a number")

        listlen = len(matrix[0])
        if any(len(row) != listlen for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")

        if div == 0:
            raise ZeroDivisionError("division by zero")

        msg = "matrix must be a matrix (list of lists) of integers/floats"
        for row in matrix:
            for i in row:
                if type(i) not in [int, float]:
                    raise TypeError(msg)

        newmatrix = []
        for j in matrix:
            newmatrix.append(list(map(lambda x: round(x / div, 2), j)))
        return newmatrix
    else:
        return matrix
