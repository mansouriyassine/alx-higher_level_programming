#!/usr/bin/python3
"""Add command-line arguments to a Python list and save it to a file."""

import sys


if __name__ == "__main__":
    from json_management import save_to_json_file, load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])

    save_to_json_file(items, "add_item.json")
