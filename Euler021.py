"""
Author: Matthias Steinwendner, 2018

Let d(n) be defined as the sum of proper divisors of n 
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b 
are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 
are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 
are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def sum_proper_divisors(n):
    if n == 1:
        return 0
    divisors = [1]
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            if i not in divisors:
                divisors.append(i)
            o = n / i
            if o not in divisors:
                divisors.append(o)
    return int(sum(divisors))


dict_sum_proper_divisors = {}
for i in range(1, 10000):
    dict_sum_proper_divisors[i] = sum_proper_divisors(i)

amicable_sum = 0
for i in range(1, len(dict_sum_proper_divisors)):
    divisor_sum = dict_sum_proper_divisors[i]
    if 0 < divisor_sum < len(dict_sum_proper_divisors) and divisor_sum != i:
        if dict_sum_proper_divisors[divisor_sum] == i:
            amicable_sum += i

print(amicable_sum)
