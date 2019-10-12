#!/usr/bin/env python3
# Character Picture Grid

grid = [
    [".", ".", ".", ".", ".", "."],
    [".", "O", "O", ".", ".", "."],
    ["O", "O", "O", "O", ".", "."],
    ["O", "O", "O", "O", "O", "."],
    [".", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "."],
    ["O", "O", "O", "O", ".", "."],
    [".", "O", "O", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
]

rows = len(grid)
columns = len(grid[0])

for x in range(columns):
    for y in range(rows):
        print(grid[y][x], end="")
    print()
