#!/usr/bin/python3

# Print num from 0 to 99, two digits and separated by a comma and space
print(", ".join("{:02d}".format(i) for i in range(100)), end='\n')
