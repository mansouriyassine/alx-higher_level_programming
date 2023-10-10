#!/usr/bin/python3


def write_file(filename="", text=""):
    """
    Writes string to a text file and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)


if __name__ == "__main__":
    # Example usage:
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
