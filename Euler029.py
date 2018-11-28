"""
Author: Matthias Steinwendner, 2018

Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

    a ^ b

If they are then placed in numerical 
order, with any repeats removed, we get the 
following sequence of 15 distinct terms:

    4, 8, 9, 16, 25, 27, 32, 64,
    81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated 
by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
"""

distinct_terms = set()

for a in range(2, 101):
    for b in range(2, 101):
        distinct_terms.add(a ** b)
print(len(distinct_terms))
