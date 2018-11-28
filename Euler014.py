"""
Author: Matthias Steinwendner, 2018

The following iterative sequence is defined for the set of positive integers:
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)
Which starting number, under one million, produces the longest chain?
"""


def size_of_collatz(n):
    if n == 1:
        return 1
    if n in values:
        return values[n]
    while n != 1:
        if n % 2 == 0:
            return 1 + size_of_collatz(n / 2)
        else:
            return 1 + size_of_collatz(3 * n + 1)


values = {}
for i in range(1, 1000000):
    values[i] = size_of_collatz(i)

print(max(values, key=values.get))
