#!/usr/bin/python3
"""
Module 5-square
Defines class Square with private instance attribute size and methods area
and my_print.
"""


class Square:
    """
    A class that defines a square by its size and can compute its area and
    print its representation using '#' characters.

    Attributes:
    size (int): The size of the square, must be an integer and >= 0.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a given size.

        Args:
        size (int): The size of the square, with a default value of 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
        value (int): The size to set for the square.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Compute the area of the square.

        Returns:
        The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' or an empty line if size is 0.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
