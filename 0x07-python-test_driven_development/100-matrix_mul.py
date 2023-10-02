#!/usr/bin/python3

"""
Matrix Multiplication

This module defines a function for matrix multiplication.

"""


def matrix_mul(m_a, m_b):
    if (not isinstance(m_a, list) or not isinstance(m_b, list) or
            not all(isinstance(n, (int, float)) for r in m_a for n in r) or
            not all(isinstance(n, (int, float)) for r in m_b for n in r) or
            not all(len(r) == len(m_a[0]) for r in m_a) or
            not all(len(r) == len(m_b[0]) for r in m_b)):
        raise TypeError('m_a and m_b should be lists of lists containing only '
                        'integers or floats and each row '
                        'should have the same size')

    if not m_a or not m_b:
        raise ValueError("m_a and m_b can't be empty")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
