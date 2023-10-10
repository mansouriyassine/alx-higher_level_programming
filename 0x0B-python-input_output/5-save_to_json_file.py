#!/usr/bin/python3
"""Defines a function to save an object to a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """Save an object to a JSON file.

    Args:
        my_obj: The object to be saved.
        filename (str): The name of the file to save to.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
