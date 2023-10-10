#!/usr/bin/python3
"""File Writer: Write a string to a UTF-8 text file."""


def write_file(filename="", text=""):
    """
    Write the provided text to a UTF-8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        chars_written = file.write(text)
        return chars_written


if __name__ == "__main__":
    filename = "my_first_file.txt"
    text = "This School is so cool!\n"
    nb_characters = write_file(filename, text)

    print(nb_characters + len("\n"))
