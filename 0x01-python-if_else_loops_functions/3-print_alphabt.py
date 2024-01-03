#!/usr/bin/python3

# Print the lowercase ASCII, skipping 'q' and 'e', in one line
print(
    "{}".format(
        ''.join(chr(i) for i in range(97, 123) if chr(i) not in 'qe')
    ),
    end=''
)
