#!/usr/bin/python3

"""
This script defiines a function for matrix division.
"""

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.

    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.

    Returns:
        A new matrix representing the result of the division.
    """

    # Check if matrix is a list of non-empty lists containing only integers or floats
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a  matrix(list of lists) of integers/float")

    #check if all the row have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    #check if div is an integer or a float
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    #check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    #Create a new matrix contaiining the results of the division
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    #return new matrix

    return new_matrix
