#!/usr/bin/python3
"""
This module divides every element of a matrix with
a number
"""


def matrix_divided(matrix, div):
    """
    This function divides every element of a matrix

    Args:
        matrix: matrix containint lists of int and float
        div: number to divide each element

    """
    er_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not matrix or not isinstance(matrix, list):
        raise TypeError(er_msg)

    mat_len = 0

    for items in matrix:
        if not items or not isinstance(items, list):
            raise TypeError(er_msg)
        if mat_len != 0 and len(items) != mat_len:
            raise TypeError("Each row of the matrix must have the same size")

        for item in items:
            if type(item) not in [int, float]:
                raise TypeError(er_msg)

        mat_len = len(items)

    lam = map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix)
    new_matrix = list(lam)
    return (new_matrix)
