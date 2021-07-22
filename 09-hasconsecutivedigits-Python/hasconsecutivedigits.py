# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	n = abs(n)
	flag = False
	pre = -1
	while(n>0):
		bef = n%10
		n //=10
		if bef == (pre - 1):
			# print(bef,pre)
			flag = True
		pre = bef
	return flag
print(hasconsecutivedigits(12210))