#!/usr/bin/python3
"""Script that takes in a URL, sends a request and displays
the value of the X-Request-Id variable found in the header"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as r:
        print(r.headers.get('X-Request-Id'))
