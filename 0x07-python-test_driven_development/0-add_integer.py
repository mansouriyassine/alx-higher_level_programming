#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int): The first integer.
        b (int, optional): The second integer, with a default value of 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not integer or
        a float that can be cast to an integer.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast a and b to integers if they are floats
    a = int(a)
    b = int(b)

    return a + b
