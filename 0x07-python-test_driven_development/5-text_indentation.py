#!/usr/bin/python3
"""
Module: 5-text_indentation

Provides text_indentation(text) function to print
a text with 2 new lines after '.', '?', and ':' characters.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?', and ':' characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If 'text' is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = 0
    for i, char in enumerate(text):
        if char in ".?:":
            print(text[start:i + 1].strip())
            print()
            start = i + 1

    if start < len(text):
        print(text[start:].strip())
