#!/usr/bin/python3
"""Defines a function for serializing a class instance to JSON."""


def class_to_json(obj):
    """Serializes a class instance to a
    dictionary for JSON serialization."""
    return obj.__dict__
