# Write the function circlesIntersect(x1, y1, r1, x2, y2, r2) 
# that takes 6 numbers (ints) -- x1, y1, r1, x2, y2, r2 -- 
# that describe the circle centered at (x1,y1) with radius r1, 
# and the circle centered at (x2,y2) with radius r2, and returns True 
# if the two circles intersect and False otherwise.
import math
def fun_circlesintersect(x1, y1, r1, x2, y2, r2):
	# your code goes here
		
	dis = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
	rad = (r1 + r2) * (r1 + r2);
	if dis==rad or dis<rad:
		return True
	else:
		return False