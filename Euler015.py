"""
Author: Matthias Steinwendner, 2018

Starting in the top left corner of a 2×2 grid, 
and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""


def possible_paths(n):
    result = 1
    for i in range(1, n):
        result = result * (n + i) / i
    return result


print(possible_paths(20))
