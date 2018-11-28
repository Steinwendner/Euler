"""
Author: Matthias Steinwendner, 2018

A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of 
the digits 1, 2, 3 and 4. If all of the permutations 
are listed numerically or alphabetically, we call it 
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation 
of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from math import factorial

perm = [i for i in range(0, 10)]
numbers = perm.copy()
N = len(perm)
final = ""
remain = int(1e6 - 1)

for i in range(1, N):
    nextNumberIndex = int(remain / factorial(N - i))
    remain = remain % factorial(N - i)
    final += str(numbers[nextNumberIndex])
    numbers.pop(nextNumberIndex)
    if remain == 0:
        break

for n in numbers:
    final += str(n)

print(final)
