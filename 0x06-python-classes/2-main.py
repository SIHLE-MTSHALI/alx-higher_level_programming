#!/usr/bin/python3
"""
Test module for Square class with size validation
"""

Square = __import__('2-square').Square

my_square_1 = Square(3)
print("Type of my_square_1: {}".format(type(my_square_1)))
print("Attributes of my_square_1: {}".format(my_square_1.__dict__))

my_square_2 = Square()
print("Type of my_square_2: {}".format(type(my_square_2)))
print("Attributes of my_square_2: {}".format(my_square_2.__dict__))

try:
    my_square_3 = Square("3")
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
except Exception as e:
    print(e)
