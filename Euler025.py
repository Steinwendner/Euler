"""
Author: Matthias Steinwendner, 2018

The Fibonacci sequence is defined by the recurrence relation:

Fn = F(n−1) + F(n−2), where F(1) = 1 and F(2) = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci 
sequence to contain 1000 digits?
"""

import time

index = 3
a = 1
b = 1
fib = a + b
while len(str(fib)) < 1000:
    a = b
    b = fib
    fib = a + b
    index += 1
t = time.process_time()

print("answer: " + str(index))
print("time needed: " + str(t) + " seconds")
