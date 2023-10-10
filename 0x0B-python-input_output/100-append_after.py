#!/usr/bin/python3
"""Defines a text file insertion function."""


def insert_text_after(file_name="", search_text="", new_text=""):
    """Insert new text after each line containing a specified text in a file.

    Args:
        file_name (str): The name of the file.
        search_text (str): The text to search for within the file.
        new_text (str): The text to insert.
    """
    updated_text = ""
    with open(file_name) as file_reader:
        for line in file_reader:
            updated_text += line
            if search_text in line:
                updated_text += new_text
    with open(file_name, "w") as file_writer:
        file_writer.write(updated_text)
