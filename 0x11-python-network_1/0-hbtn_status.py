#!/usr/bin/python3
"""
Fetches the status of a given URL and displays various attributes of
the response body, including its type, raw content, and utf-8 decoded
content.
"""

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    content = response.read()
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", content.decode('utf-8'))
