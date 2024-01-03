#!/usr/bin/python3

# Use nested loops to generate each combination of two different digits
for i in range(10):
    for j in range(i + 1, 10):
        if i < 8:  # To avoid a comma and space after the last number
            print("{:02d}, ".format(i * 10 + j), end='')
        else:
            print("{:02d}".format(i * 10 + j), end='\n')
