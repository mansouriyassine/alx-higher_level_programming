#!/usr/bin/python3
"""Read file """


def read_file(filename=""):
    """Reads content.

    Args:
        filename (str): name of file

    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
