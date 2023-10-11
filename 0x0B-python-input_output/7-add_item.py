#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys

if __name__ == "__main__":
    from json_file_utils import save_to_json_file, load_from_json_file

    try:
        existing_items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_items = []

    new_items = sys.argv[1:]
    combined_items = existing_items + new_items
    save_to_json_file(combined_items, "add_item.json")
