#!/usr/bin/python3
"""Add items to a JSON file."""

import sys
from json_file_utils import save_to_json_file, load_from_json_file


def add_items_to_json(file_path, items):
    try:
        existing_content = load_from_json_file(file_path)
    except FileNotFoundError:
        existing_content = []

    existing_content.extend(items)

    save_to_json_file(existing_content, file_path)

    print("Items added successfully!")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./7-add_item.py <item1> <item2> ...")
    else:
        items_to_add = sys.argv[1:]
        add_items_to_json("add_item.json", items_to_add)
