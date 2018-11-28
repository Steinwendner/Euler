"""
Author: Matthias Steinwendner, 2018

Find the sum of all the primes below two million.
"""


def is_prime(n, primes):
    """
        Returns True if the given number is a prime, False otherwise

        n:          The number to check for
        :primes:    Has to be a list with all prime numbers < n
    """
    for p in primes:
        if n % p == 0:
            return False
    return True


# straight forward prime evaluation, skipping even numbers, starting at 3
primes_sum = 2
prime_collection = [2]
for i in range(3, 2000000, 2):
    if is_prime(i, prime_collection):
        primes_sum += i
        prime_collection.append(i)
print(primes_sum)
