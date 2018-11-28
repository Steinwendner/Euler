""""
Author: Matthias Steinwendner, 2018

Find the thirteen adjacent digits in the 1000-digit number that
have the greatest product. What is the value of this product?
"""

from functools import reduce
from operator import mul


# read the 1000 digit number from a file
with open("assets/Euler008.txt") as data:
    # save every character in the string (except line breaks) into an int field
    nos = [int(c) for line in data for c in line if c != '\n']

# split the digit into 13 digit segments and calculate the product of each one
print(max([reduce(mul, nos[i:i + 13]) for i in range(len(nos) - 13)]))
