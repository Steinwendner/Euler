"""
Author: Matthias Steinwendner, 2018

A perfect number is a number for which the sum of its 
proper divisors is exactly equal to the number. For example, 
the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors 
is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two abundant 
numbers is 24. By mathematical analysis, it can be shown that all 
integers greater than 28123 can be written as the sum of two 
abundant numbers. However, this upper limit cannot be reduced 
any further by analysis even though it is known that the 
greatest number that cannot be expressed as the sum of two 
abundant numbers is less than this limit.

Find the sum of all the positive integers which 
cannot be written as the sum of two abundant numbers.

"""

from math import sqrt
from functools import reduce
from operator import add


def proper_divisors(n):
    """ returns every divisor of n except n """
    if n == 1:
        return []
    divisors = [1]
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            if i not in divisors:
                divisors.append(i)
                if n / i != i:
                    divisors.append(n / i)
    return divisors


# check which of the first 28124 number are abundant
abundant = []
for i in range(12, 28124):
    if sum(proper_divisors(i)) > i:
        abundant.append(i)
print("abundant numbers found")

# calculate all possible sums
sums = set()
for i in range(0, len(abundant)):
    for j in range(i, len(abundant)):
        tmp = abundant[i] + abundant[j]
        if tmp > 28124:
            break
        sums.add(tmp)
print("abundant sums calculated")

# sum up everything, that can't be expressed as a sum of 2 abundant numbers
other = set(range(1, 28124))
final = list(other - sums)
print(reduce(add, final))
