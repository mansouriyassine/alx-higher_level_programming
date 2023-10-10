#!/usr/bin/python3
"""String to JSON Converter: Convert a string object to its JSON representation."""
import json


def to_json_string(my_obj):
    """
    Convert a Python object to its JSON representation as a string.

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
