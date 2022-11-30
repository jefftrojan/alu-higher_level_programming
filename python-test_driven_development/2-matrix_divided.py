#!/usr/bin/python3
""" A function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ Func divides a list of lists """

    if not isinstance(matrix, int) and not isinstance(matrix, float):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    matrix_length = len(matrix)
    for i in range(matrix_length):
        if matrix != matrix_length:
           raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number ")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    matrix = int
    div = int
    new_matrix = matrix/div
    new_matrix = round(new_matrix, 2)

    return (new_matrix)
