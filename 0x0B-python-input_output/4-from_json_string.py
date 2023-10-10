#!/usr/bin/python3
import json


def from_json_string(my_str):
    """
    Convert a JSON string to a Python data structure.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
