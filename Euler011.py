"""
Author: Matthias Steinwendner, 2018

What is the greatest product of four adjacent numbers in the same 
direction (up, down, left, right, or diagonally) in the 20×20 grid?
"""

from operator import mul
from functools import reduce

# number of adjacent digits to sum up
SPAN = 4

# loading the grid into a two dimensional array
grid = None
with open("assets/Euler011.txt") as data:
    for line in data:
        grid.append(list(map(int, line.split())))

products = []

# horizontal
for row in grid:
    products.extend([reduce(mul, row[i:i + SPAN]) for i in range(len(row) - SPAN)])

# vertical
for c in range(len(grid[0])):
    products.extend([reduce(mul, grid[c][i:i + SPAN]) for i in range(len(grid) - SPAN)])

# diagonal top left to bottom right
for r in range(len(grid) - SPAN + 1):
    for c in range(len(grid[r]) - SPAN + 1):
        tmp = [grid[r][c], grid[r + 1][c + 1], grid[r + 2][c + 2], grid[r + 3][c + 3]]
        print(tmp)
        products.append(reduce(mul, tmp))

# diagonal top right to bottom left
for r in range(len(grid) - SPAN + 1):
    for c in reversed(range(SPAN - 1, len(grid[r]))):
        tmp = [grid[r][c], grid[r + 1][c - 1], grid[r + 2][c - 2], grid[r + 3][c - 3]]
        products.append(reduce(mul, tmp))

print(str(len(products)) + " products calculated")
print("with " + str(reduce(max, products)) + " being the highest")
