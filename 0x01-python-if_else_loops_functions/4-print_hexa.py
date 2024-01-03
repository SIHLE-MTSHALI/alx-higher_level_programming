#!/usr/bin/python3

# Print numbers from 0 to 98 in decimal and hexadecimal
print("\n".join("{} = {}".format(i, hex(i)) for i in range(99)), end='\n')
