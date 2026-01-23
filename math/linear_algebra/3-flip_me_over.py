#!/usr/bin/env python3
"""Module for transposing matrices"""


def matrix_transpose(matrix):
    return [list(row) for row in zip(*matrix)]
