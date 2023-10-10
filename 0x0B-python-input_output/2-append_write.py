#!/usr/bin/python3
"""File Appender: Append a string to the end of a UTF-8 text file."""


def append_write(filename="", text=""):
    """
    Append the provided text to a UTF-8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to be appended to the file.

    Returns:
        int: The number of characters appended to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        chars_appended = file.write(text)
        return chars_appended
