"""
Author: Matthias Steinwendner, 2018

Problem
What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?


No need to hard code anything, 
we will simply find the smallest common multiple
between the first 20 digits beginning from 1.
"""

import math
import functools
from operator import mul

def prime_factorization(n):
    """
    Returns a dictionary with the prime factors of the given number,
    where the keys are the prime factor and it's values are the number
    of occurrences.
    """
    prime_factors = {}

    while n % 2 == 0:
        if 2 in prime_factors:
            prime_factors[2] = prime_factors[2] + 1
        else:
            prime_factors[2] = 1
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            if i in prime_factors:
                prime_factors[i] = prime_factors[i] + 1
            else:
                prime_factors[i] = 1
            n = n / i
    if n > 2:
        if n in prime_factors:
            prime_factors[n] = prime_factors[n] + 1
        else:
            prime_factors[n] = 1
    return prime_factors


# create 20 dictionaries with the prime factors of each digit
numbers = [prime_factorization(r) for r in range(1, 21)]

# find the highest power of every prime factor
lcm = {}
for d in numbers:
    for key in d:
        if key not in lcm or d[key] > lcm[key]:
            lcm[key] = d[key]

# compute the lcm by multiplying all prime factors with their highest power
result = functools.reduce(mul, [key ** lcm[key] for key in lcm])

print(result)
