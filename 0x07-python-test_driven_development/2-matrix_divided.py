#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divide elements of a matrix by a divisor.

    Args:
        matrix (list of lists): Input matrix.
        div (int or float): Divisor (non-zero).

    Returns:
        list of lists: New matrix with rounded results.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows of the matrix have different sizes.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.

    Example:
        >>> matrix = [
        ...     [1, 2, 3],
        ...     [4, 5, 6]
        ... ]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists of integers/floats")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        result.append(new_row)

    return result


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
