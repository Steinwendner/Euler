"""
Author: Matthias Steinwendner, 2018

Work out the first ten digits of the sum of the 
following one-hundred 50-digit numbers.
(numbers were saved separately)
"""


from functools import reduce
from operator import add


summands = []
with open("assets/Euler013.txt", "r") as data:
	for line in data:
		summands.append(int(line))

result = reduce(add, summands)
print(str(result)[:10])
