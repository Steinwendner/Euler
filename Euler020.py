"""
Author: Matthias Steinwendner, 2018

Find the sum of the digits in the number 100!
"""


from math import factorial
from functools import reduce
from operator import add

print(reduce(add, [int(x) for x in str(factorial(100))]))
