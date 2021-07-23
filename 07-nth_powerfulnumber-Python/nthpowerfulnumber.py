# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

# import math

# def powerful(n):
# 	while (n % 2 == 0):
# 		power = 0
# 		while (n % 2 == 0):
# 			n = n // 2
# 			power = power + 1
# 		if (power == 1):
# 			return False
# 	for i in range(3, int(math.sqrt(n))+1, 2):
# 		power = 0
# 		while (n % i == 0):
# 			n = n // i
# 			power = power + 1
# 		if (power == 1):
# 			return False
# 	return (n == 1)

# def nthpowerfulnumber(n):
# 	# Your code goes here
# 	count = 0
# 	i = 0
# 	while (count <= abs(n)):
# 		i += 1
# 		if(powerful(i)):
# 			count += 1
# 	return i

def isprime(x):
    count=0
    if x>1:
        for i in range(1,x+1):
            if(x%i)==0:
                count = count+1
        if count == 2:
            return True
        else:
            return False
def powerfulnumber(x):
    if(x==1):
        return True
    
    else:
        
        count=0
        count2=0
        for i in range(2,int(x/2)+1):
            if(x%i==0 and isprime(i)):
                count+=1
                if(x%(i*i)==0):
                    count2+=1
        print(count,count2)
        if(count==0 or count2==0):
            return False
        elif(count==count2):
            return True

    return False

def nthpowerfulnumber(n):

    found = 0
    guess = 0
    while (found <= abs(n)):
        guess += 1
        if(powerfulnumber(guess)):
            found += 1
    return guess
