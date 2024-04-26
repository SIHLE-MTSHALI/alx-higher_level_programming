#!/usr/bin/python3
"""
Sends a GET request to a specified URL and retrieves the `X-Request-Id`
header value from the response. The URL is passed as a command-line
argument.
"""

import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    print(response.info().get('X-Request-Id'))
