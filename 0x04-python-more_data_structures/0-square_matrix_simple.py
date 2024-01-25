#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_output = []

    for row in matrix:
        row_output = []

        for element in row:
            squared_element = element ** 2
            row_output.append(squared_element)

        matrix_output.append(row_output)

    return matrix_output
