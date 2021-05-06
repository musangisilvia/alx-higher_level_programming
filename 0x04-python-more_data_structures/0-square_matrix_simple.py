#!/usr/bin/python3


from copy import deepcopy


# square_matrix_simple - computes the square value of all ints if a matrix.
def square_matrix_simple(matrix=[]):
    new_matrix = deepcopy(matrix)
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            new_matrix[i][j] *= new_matrix[i][j]
    return new_matrix
