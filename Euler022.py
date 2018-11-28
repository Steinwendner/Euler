"""
Author: Matthias Steinwendner, 2018

Using names.txt (saved it under assets/Euler018.py), 
a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the 
list to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 
938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""


def value_of_string(name):
    value = 0
    for c in name:
        value += ord(c) - ord("A") + 1
    return value


with open("assets/Euler022.txt", "r") as file:
    data = file.read()

data = data.replace("\"", "")
names = data.split(",")
names.sort()

name_scores_sum = 0
for i in range(0, len(names)):
    name_scores_sum += (i + 1) * value_of_string(names[i])

print(name_scores_sum)
