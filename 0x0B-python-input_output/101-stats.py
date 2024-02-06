#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
"""

import sys

status_c = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        data = line.split()
        if len(data) > 2:
            status_code = data[-2]
            file_size = data[-1]

            if status_code in status_c:
                status_c[status_code] += 1

            total_size += int(file_size)
            line_count += 1

            if line_count % 10 == 0:
                print("File size: {}".format(total_size))
                for code in sorted(status_c.keys()):
                    if status_c[code]:
                        print("{}: {}".format(code, status_c[code]))

except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for code in sorted(status_c.keys()):
        if status_c[code]:
            print("{}: {}".format(code, status_c[code]))
    raise

print("File size: {}".format(total_size))
for code in sorted(status_c.keys()):
    if status_c[code]:
        print("{}: {}".format(code, status_c[code]))
