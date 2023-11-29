#!/usr/bin/python3
"""defines functions"""


def generate_pascals_row():
    """generate rows for the pascal
triangle"""
    row = [1]
    while True:
        yield row
        row = [1] + [row[j] + row[j + 1] for j in range(len(row) - 1)] + [1]


def pascal_triangle(n):
    """return the pascal rep of the
    value n passed as the parameter"""
    if n <= 0:
        return []
    triangle = []
    row_generator = generate_pascals_row()
    for i in range(n):
        triangle.append(next(row_generator))
    return triangle
