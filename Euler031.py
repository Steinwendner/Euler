"""
Author: Matthias Steinwendner, 2018

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

"""


def count(n, m, values):
    """
    Returns the number of possible ways to combine the elements of a list,
    so that their sum equals n.

    :param n: Target Value
    :param m: Index of the element to check
    :param values: List of possible values
    :return: Returns all possible combinations of values to get the target
    """
    if n < 0 or m < 0:
        return 0
    elif n == 0:
        return 1

    return count(n, m - 1, values) + count(n - values[m], m, values)


coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200
print(count(target, len(coins)-1, coins))
