#!/usr/bin/python3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    """
    try:
        result = np.dot(np.array(m_a), np.array(m_b))
        return result
    except ValueError as ve:
        raise ValueError("m_a and m_b can't be multiplied") from ve
