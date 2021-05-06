#!/usr/bin/python3


# square_matrix_simple - computes the square value of all ints if a matrix.
def square_matrix_simple(matrix=[]):
    new_matrix = [[0 for _ in range(len(matrix[0]))]
    for _ in range(len(matrix))]
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            new_matrix[i][j] = matrix[i][j]*matrix[i][j]
    return new_matrix
