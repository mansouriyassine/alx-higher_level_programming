#!/usr/bin/python3
"""File Reader Module"""


def read_and_print_file(filename=""):
    """Reads a text file and prints its content to the console."""
    with open(filename, "r", encoding="utf-8") as file_to_read:
        for line in file_to_read:
            print(line, end="")
