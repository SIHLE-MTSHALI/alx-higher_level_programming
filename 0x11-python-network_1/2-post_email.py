#!/usr/bin/python3
"""
Sends a POST request to a specified URL with an email parameter and
displays the response body (decoded in utf-8). The URL and email
parameter are passed as command-line arguments.
"""

import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')

with urllib.request.urlopen(url, data) as response:
    content = response.read()
    print(content.decode('utf-8'))
