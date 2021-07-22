# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

import math

def powerful(n):
	while (n % 2 == 0):
		power = 0
		while (n % 2 == 0):
			n = n // 2
			power = power + 1
		if (power == 1):
			return False
	for i in range(3, int(math.sqrt(n))+1, 2):
		power = 0
		while (n % i == 0):
			n = n // i
			power = power + 1
		if (power == 1):
			return False
	return (n == 1)

def nthpowerfulnumber(n):
	# Your code goes here
	count = 0
	i = 0
	while (count <= abs(n)):
		i += 1
		if(powerful(i)):
			count += 1
	return i