#!/usr/bin/python3
"""
Module 7-base_geometry updates the BaseGeometry class with a public instance
method for validating integer values.
"""


class BaseGeometry:
    """
    A class BaseGeometry with enhanced public instance methods.
    """

    def area(self):
        """Raises an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is an integer greater than 0.
        
        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
