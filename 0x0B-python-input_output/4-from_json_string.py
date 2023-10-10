#!/usr/bin/python3
"""Defines a JSON string-to-object function."""
import json


def from_json_string(my_str):
    """Convert a JSON string to a Python object.

    Args:
        my_str (str): JSON string to be converted.

    Returns:
        obj: Python object represented by the JSON string.
    """
    return json.loads(my_str)
