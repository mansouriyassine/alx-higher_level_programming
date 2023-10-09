#!/usr/bin/python3
"""Defines a function to check if an object is an instance of a specified class."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specified class."""
    return type(obj) is a_class
