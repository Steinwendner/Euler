"""
Author: Matthias Steinwendner, 2018

How many Sundays fell on the first of the month during 
the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

from datetime import *

counter = 0
d = datetime(1901, 1, 1)
while d != datetime(2000, 12, 31):
    if d.day == 1 and d.weekday() == 6:
        counter += 1
    d += timedelta(days=1)

print(counter)
