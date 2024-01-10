#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Function to square the values in a 2D matrix.
    Args:
        matrix: A list of lists where each sublist represents a matrix row.
    Returns:
        A new matrix with each value squared.
    """
    return [list(map(lambda x: x**2, row)) for row in matrix]
