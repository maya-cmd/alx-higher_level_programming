#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    return list(map(lambda y: list(map(lambda a: a ** 2, y)), matrix))
