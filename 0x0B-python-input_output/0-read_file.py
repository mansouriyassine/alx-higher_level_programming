#!/usr/bin/python3

def read_file(filename=""):
    """Reads a text file (UTF8) and prints its content to stdout."""
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end='')


if __name__ == "__main__":
    read_file("my_file_0.txt")
