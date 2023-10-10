#!/usr/bin/python3
"""Adds command line arguments to a
Python list and saves to a JSON file."""
import sys
import os.path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

args = sys.argv[1:]

filename = "add_item.json"

if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

my_list.extend(args)
save_to_json_file(my_list, filename)
