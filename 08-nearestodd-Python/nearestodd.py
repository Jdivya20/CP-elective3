# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.

def isodd(n):
	if n%2!=0:
		return True
	else:
		return False


def fun_nearestodd(n):
	n1=int(n)
	before=n1-1
	after=n1+1
	if isodd(before) and isodd(after) and n-before==after-n:
		return before
	elif n-before<after-n and isodd(before) and isodd(after):
		return before
	elif n-before>after-n and isodd(before) and isodd(after):
		return after
	else:
		return n1


