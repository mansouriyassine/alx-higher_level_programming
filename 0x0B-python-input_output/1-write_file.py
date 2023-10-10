#!/usr/bin/python3



def write_file(filename="", text=""):
    """Write a string to a text file (UTF-8) and return the number
       of characters written. Existing content is overwritten.

    Args:
        filename (str): The name of the file to be opened.
        text (str): The characters to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        chars_written = file.write(text)
        return chars_written
