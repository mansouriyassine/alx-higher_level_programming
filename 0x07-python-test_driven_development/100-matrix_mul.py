#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list[list[int or float]]): First matrix.
        m_b (list[list[int or float]]): Second matrix.

    Returns:
        list[list[int or float]]: Result of matrix multiplication.

    Raises:
        TypeError: If input matrices are not valid lists of lists.
        ValueError: If input matrices have incompatible dimensions.
    """
    # Check if m_a and m_b are lists of lists
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if m_a and m_b are not empty
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty" if not m_a else "m_b can't be empty")

    # Check if elements of m_a are integers or floats
    if not all(isinstance(val, (int, float)) for row in m_a for val in row):
        raise TypeError("m_a should contain only integers or floats")

    # Check if elements of m_b are integers or floats
    if not all(isinstance(val, (int, float)) for row in m_b for val in row):
        raise TypeError("m_b should contain only integers or floats")

    # Get the dimensions of m_a and m_b
    a_rows, a_cols = len(m_a), len(m_a[0])
    b_rows, b_cols = len(m_b), len(m_b[0])

    # Check if the number of columns in m_a is equal to the number of rows in m_b
    if a_cols != b_rows:
        raise ValueError("m_a and m_b can't be multiplied")

    # Initialize the result matrix with zeros
    result_matrix = [[0 for _ in range(b_cols)] for _ in range(a_rows)]

    # Perform matrix multiplication
    for i in range(a_rows):
        for j in range(b_cols):
            for k in range(a_cols):
                result_matrix[i][j] += m_a[i][k] * m_b[k][j]

    return result_matrix

