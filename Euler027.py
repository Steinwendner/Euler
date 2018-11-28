"""
Author: Matthias Steinwendner, 2018

Euler discovered the remarkable quadratic formula:

n2+n+41
It turns out that the formula will produce 40 primes for 
the consecutive integer values 0≤n≤39. However, 
when n=40,402+40+41=40(40+1)+41 is divisible by 41, 
and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, 
which produces 80 primes for the consecutive values 0≤n≤79. 
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the 
quadratic expression that produces the maximum number 
of primes for consecutive values of n, starting with n=0.
"""
import time


def consecutive_primes(a, b, prime_numbers):
    """
        Returns the count of the consecutive primes using
        the formula:
                    n^2+an+b
    """
    n = 0
    counter = 0
    q = n ** 2 + a * n + b
    if q > 0:
        while q in prime_numbers:
            n += 1
            counter += 1
            q = n ** 2 + a * n + b
    return counter


def is_prime(n):
    """ Returns True if the given number is a prime, False otherwise """
    global primes
    if len(primes) > 0:
        if n < primes[-1]:
            if n in primes:
                return True

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


def calc_primes(limit, target_list):
    """ Calculates all primes up to the specified limit """

    for i in range(1, limit):
        if is_prime(i):
            target_list.append(i)


primes = []
calc_primes(1000, primes)
print(str(len(primes)) + " primes found")

maxA = 0
maxB = 0
maxVal = 0
for a in range(-1000, 1000):
    for b in primes:
        if b in primes:
            if a % 2 != 0:
                if a >= 1 - b:
                    val = consecutive_primes(a, b, primes)
                    if val > maxVal:
                        maxA, maxB, maxVal = a, b, val
result = maxA * maxB
print(result)
print("calculation took {} seconds".format(time.process_time()))
