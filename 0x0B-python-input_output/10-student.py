#!/usr/bin/python3
"""
Defines a Student class.
"""


class Student:
    """
    Represents a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.
        Args:
            first_name (str): The first name.
            last_name (str): The last name.
            age (int): The age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        Filters attributes if attrs is a list of strings, otherwise,
        all attributes are retrieved.
        Args:
            attrs (list): Attributes to retrieve, if specified.
        Returns:
            A dictionary representation of the Student instance.
        """
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            filtr_dict = {k: v for k, v in self.__dict__.items() if k in attrs}
            return filtr_dict
        return self.__dict__
