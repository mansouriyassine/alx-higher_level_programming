#!/usr/bin/python3

"""
This module defines a class called LockedClass, which enforces
strict attribute control, allowing only 'first_name' as a valid attribute.
"""


class LockedClass:
    """
    LockedClass ensures strict control over attribute creation,
    allowing only 'first_name' as an acceptable attribute.
    """
    __slots__ = ["first_name"]
