"""
Author: Matthias Steinwendner, 2018

What is the 10 001st prime number?
"""


def is_prime(n):
    """ Returns True if the given number is a prime, False otherwise """
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


target_position = 10001

# we start at 3, 1 and 2 are already counted as primes
primes_found = 2
i = 3
while True:
    i += 2
    if is_prime(i):
        primes_found += 1
        if primes_found == target_position:
            print(i)
            break
