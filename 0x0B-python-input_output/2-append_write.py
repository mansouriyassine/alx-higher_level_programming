#!/usr/bin/python3


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text
    file and returns the number of characters added.

    Args:
        filename (str): The name of the file to which text will be appended.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        chars_added = file.write(text)
        return chars_added


if __name__ == "__main__":
    filename = "file_append.txt"
    text = "This School is so cool!\n"
    nb_characters_added = append_write(filename, text)

    print(nb_characters_added)
