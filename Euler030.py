"""
Author: Matthias Steinwendner, 2018

Surprisingly there are only three numbers that 
can be written as the sum of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be 
written as the sum of fifth powers of their digits.
"""

"""
Thought process:

To get the highest possible sum for a number with x digits
we simply have to calculate:

    x * 9^5

Knowing this we can say there are no number with 7 digits,
where the sum of its digits by the power of 5 equals the number.

Lowest possible number with 7 digits:

    1000000

Highest possible sum of it's digits by the power of 5:

    7*9^5  =  413343

And given that 6*9^5 equals 354294, we only have to check for numbers
up to this limit.
"""


def digit_pow_sum(n):
    dps = 0
    for d in str(n):
        dps += int(d) ** 5
    return dps


equal = []
for i in range(2, 6 * 9 ** 5):
    if digit_pow_sum(i) == i:
        equal.append(i)
print(equal)
print("sum: {}".format(sum(equal)))
