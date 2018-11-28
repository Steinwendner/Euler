"""
Author: Matthias Steinwendner, 2018

If all the numbers from 1 to 1000 (one thousand) inclusive were 
written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 
(three hundred and forty-two) contains 23 letters and 115 
(one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers 
is in compliance with British usage.
"""

from math import floor


def number_written(n, reference):
    written = ""
    if n <= 19 or (n % 10 == 0 and n < 100):
        return reference[n]

    if n < 100:
        tenner = int(n / 10) * 10
        written = written + reference[tenner]
        onner = int(n % 10)
        written = written + reference[onner]
        return written

    if n % 100 == 0:
        return reference[n / 100] + "hundred"

    return number_written(floor(n / 100) * 100, reference) + "and" + number_written(n % 100, reference)


numberStrings = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred"
}
char_sum = 0
for i in range(1, 1000):
    s = number_written(i, numberStrings)
    char_sum += len(s)
    print(s)
char_sum += len("onethousand")
print(char_sum)
