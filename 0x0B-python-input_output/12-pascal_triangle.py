#!/usr/bin/python3
"""
This script defines a function to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle of size n.

    Returns a list of lists representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) < n:
        row = [1]
        last_row = triangle[-1]
        for i in range(len(last_row) - 1):
            row.append(last_row[i] + last_row[i + 1])
        row.append(1)
        triangle.append(row)

    return triangle
