#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix: A list of lists of integers or floats.
        div: The divisor, must be a number (int or float) and not zero.

    Returns:
        A new matrix all elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
                   if rows of the matrix are not of the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not all(isinstance(row, list) and all(isinstance(elem, (int, float))
               for elem in row) for row in matrix):
        raise TypeError("matrix must be a (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
