#!/usr/bin/python3

# Print ASCII alphabet in reverse, alternating lowercase and uppercase
print("{}".format(''.join(chr(i) if i % 2 == 0 else chr(i - 32)
                          for i in range(122, 96, -1))), end='')
