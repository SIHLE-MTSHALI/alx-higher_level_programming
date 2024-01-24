#!/usr/bin/python3
"""
Test module for Square class with area method
"""

Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area of my_square_1: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area of my_square_2: {}".format(my_square_2.area()))
