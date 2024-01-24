#!/usr/bin/python3
"""
Module 1-square
Defines class Square with private instance attribute size.
"""


class Square:
    """
    A class that defines a square by its size.

    Attributes:
    size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes the square with a given size.

        Args:
        size (int): The size of the square.
        """
        self.__size = size
