#!/usr/bin/python3
"""
Module for lazy matrix multiplication using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a: The first matrix.
        m_b: The second matrix.

    Returns:
        A new matrix which is the product of m_a and m_b using NumPy.
    """
    return np.matmul(m_a, m_b)
