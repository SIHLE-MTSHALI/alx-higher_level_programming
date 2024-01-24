#!/usr/bin/python3
import math


class MagicClass:
    """
    Class that defines a circle with methods to calculate its area and
    circumference.
    """

    def __init__(self, radius=0):
        """
        Initialize the MagicClass with a radius.

        Args:
        radius (int or float): The radius of the circle.

        Raises:
        TypeError: If radius is not an int or float.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
        The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate the circumference of the circle.

        Returns:
        The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
