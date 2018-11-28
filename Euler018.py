"""
Author: Matthias Steinwendner, 2018

By starting at the top of the triangle below and moving to adjacent 
numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
(Triangle is saved in assets/Euler018.txt)
"""

# load the tree from a file and flip it
with open("assets/Euler018.txt", "r") as file:
    data = file.read()
tree = []
for line in data.split("\n"):
    tree.append([int(number) for number in line.split()])
tree = tree[::-1]

# calculate the maximum path by summing all nodes
for i in range(1, len(tree)):
    for j in range(0, len(tree[i])):
        tree[i][j] += max(tree[i - 1][j], tree[i - 1][j + 1])

print(tree[-1][0])
