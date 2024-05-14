#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        result = ""
        for num in row:
            result += "{:d}".format(num) + " "
        print(result[:-1])
