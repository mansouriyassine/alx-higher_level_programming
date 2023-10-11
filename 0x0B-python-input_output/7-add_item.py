#!/usr/bin/python3
"""Add items to a JSON file."""

from sys import argv
from json_file_utils import save_to_json_file, load_from_json_file

arguments = argv[1:]

try:
    existing_content = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_content = []

for argument in arguments:
    existing_content.append(argument)

save_to_json_file(existing_content, "add_item.json")
