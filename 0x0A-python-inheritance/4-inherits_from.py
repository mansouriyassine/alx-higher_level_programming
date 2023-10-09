#!/usr/bin/python3
"""check if an object is an instance of a subclass of a specified class."""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a subclass of a specified class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
