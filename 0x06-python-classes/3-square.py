#!/usr/bin/python3
"""
Module 3-square
Defines class Square with private instance attribute size and public method.
"""


class Square:
    """
    A class that defines a square by its size and can compute its area.

    Attributes:
    size (int): The size of the square, must be an integer and >= 0.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a given size.

        Args:
        size (int): The size of the square, with a default value of 0.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Compute the area of the square.

        Returns:
        The area of the square.
        """
        return self.__size ** 2
