#!/urs/bin/python3

def square_matrix_simple(matrix=[]):

    new_matrix = []
    if len(matrix) == 0:
        return new_matrix

    new_matrix = [[i**2 for i in j] for j in matrix]
    return new_matrix
