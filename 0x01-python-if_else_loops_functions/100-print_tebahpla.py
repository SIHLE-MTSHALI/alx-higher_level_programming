#!/usr/bin/python3

# Print the ASCII alphabet in reverse order, alternating lowercase and uppercase
print(
        "".join(chr(i - 32) 
            if i % 2 == 0 
            else
            chr(i) 
            for i in range(122, 96, -1)), end='')
