"""
Author: Matthias Steinwendner, 2018

By considering the terms in the Fibonacci sequence whose values 
do not exceed four million, find the sum of the even-valued terms.
"""


def next_fib(last, current):
    return last + current


last = current = 1
fib_sum = 0

while current < 4000000:
    if current % 2 == 0:
        fib_sum += current

    n = next_fib(last, current)
    last = current
    current = n

print(fib_sum)
