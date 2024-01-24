#!/usr/bin/python3
"""
Module 101-square
Defines class Square with size and position and methods to calculate the area
and print the square.
"""


class Square:
    """
    Represents a square with private instance attributes size and position.

    Attributes:
    size (int): The size of the square, must be an integer and >= 0.
    position (tuple): Position of the square as a tuple of 2 positive integers.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square.

        Args:
        size (int): The size of the square, with a default value of 0.
        position (tuple): The position of the square, default is (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieves the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
        value (tuple): The position to set for the square.

        Raises:
        TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            [print("") for _ in range(self.__position[1])]
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Defines the print() representation of the Square instance.
        """
        if self.__size == 0:
            return ""
        square_str = "\n" * self.__position[1]
        for _ in range(self.__size):
            square_str += " " * self.__position[0] + "#" * self.__size + "\n"
        return square_str.rstrip()
