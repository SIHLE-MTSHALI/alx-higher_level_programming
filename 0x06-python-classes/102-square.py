#!/usr/bin/python3
"""
Module 102-square
Defines a class Square with size property, area method comparison operators.
"""


class Square:
    """
    Class that defines a square with size, area, and comparison capabilities.

    Attributes:
    size (float or int): The size of the square, must be a number and >= 0.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a given size.

        Args:
        size (float or int): The size of the square.
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
        value (float or int): The size to set for the square.

        Raises:
        TypeError: If value is not a number.
        ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
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

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
