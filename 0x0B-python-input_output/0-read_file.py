#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file_to_read:
        content = file_to_read.read()
    return content
