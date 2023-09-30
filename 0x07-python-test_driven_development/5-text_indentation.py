def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = ['.', '?', ':']
    line = ""

    for char in text:
        line += char
        if char in punctuation_marks:
            print(line.strip())
            print()
            line = ""

    if line:
        print(line.strip())
