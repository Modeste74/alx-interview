#!/usr/bin/python3
"""defines a function island_perimeter"""


def island_perimeter(grid):
    """takes in a grid(matrix) and returns the perimeter of
    the island based of the grid passed"""
    if not grid or not grid[0]:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
    return perimeter
