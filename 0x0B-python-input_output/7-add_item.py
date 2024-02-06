#!/usr/bin/python3
"""
A script that adds all arguments to a Python list, and then save
them to a file in JSON format.
"""
import sys

# Import functions from previous tasks
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    # Load existing items from file
    items = load_from_json_file(filename)
except FileNotFoundError:
    # Initialize an empty list if file doesn't exist
    items = []

# Add command-line arguments to the list, excluding the script name
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
