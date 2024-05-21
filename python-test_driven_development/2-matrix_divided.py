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
        TypeError: If matrix is not a type list,
        or if size of matrix's row isn't same, or if div is not a number.
        ZeroDivisionError: If div equals 0.
    """
    if not isinstance(matrix, list):
        print("matrix must be a matrix (list of lists) of integers/floats")
        raise (TypeError)
    if not all(isinstance(row, list) for row in matrix):
        print("matrix must be a matrix (list of lists) of integers/floats")
        raise (TypeError)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_size = set(len(row) for row in matrix)
    if len(row_size) != 1:
        print("Each row of the matrix must have the same size")
        raise (TypeError)

    new_matrix = []
    for row in matrix:
        new_row = []
        for i in row:
            result = round(i / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)

    return (new_matrix)
