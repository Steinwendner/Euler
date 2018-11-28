"""
Author: Matthias Steinwendner, 2018

Find the largest palindrome made from the product of two 3-digit numbers.
"""

palindromes = []
span = range(100, 1000)

for i in span:
	for j in span:
		product = i*j
		if product not in palindromes:
			product_as_string = str(product)
			if product_as_string == product_as_string[::-1]:
				palindromes.append(product)
				
print(max(palindromes))
