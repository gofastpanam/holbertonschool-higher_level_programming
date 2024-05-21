#!/usr/bin/python3
"""
This module provide a function matrix_divided,
that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Create a new matrix with each num in the matrix divised by div
    and rounded to 2 decimal places.
    Args:
        matrix: The list of numbers.
        div: The divisor.
    Returns:
        The new matrix with each num in the matrix divised by div
        and rounded to 2 decimal places.
    Raises:
        TypeError: If matrix is not a type list or if div is not a number.
        ZeroDivisionError: If div equals 0.
    """
    if not isinstance(matrix, list):
        print("matrix must be a matrix (list of lists) of integers/floats")
        raise (TypeError)
    if not isinstance(div, int) and not isinstance(div, float):
        print("div must be a number")
        raise (TypeError)
    if div is 0:
        print("division by zero")
        raise (ZeroDivisionError)

    new_matrix = []
    for row in matrix:
        new_row = []
        for i in row:
            result = round(i / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)

    return (new_matrix)
