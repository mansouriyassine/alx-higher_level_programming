#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replace all occurrences of an element with another element in a new list.

    Args:
        my_list (list): The initial list.
        search: The element to search for and replace.
        replace: The new element to replace with.

    Returns:
        list: A new list with the specified replacements.
    """
    new_list = [replace if x == search else x for x in my_list]
    return new_list
