#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def generate_pascals_triangle(n):
    """Generate Pascal's Triangle of size n as a list of lists.

    Args:
        n (int): The number of rows for the Pascal's Triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        current_row = triangle[-1]
        new_row = [1]

        for i in range(len(current_row) - 1):
            new_row.append(current_row[i] + current_row[i + 1])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
