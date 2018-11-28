"""
Author: Matthias Steinwendner, 2018

What is the largest prime factor of the number 600851475143 ?
"""

import math


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


upper_bound = 600851475143
highest_prime_factor = None
# go through all primes up until sqrt(upper_bound), skip even numbers
for x in range(1, math.floor(math.sqrt(upper_bound)) + 1, 2):
    if is_prime(x) and upper_bound % x == 0:
        highest_prime_factor = x
print(highest_prime_factor)

