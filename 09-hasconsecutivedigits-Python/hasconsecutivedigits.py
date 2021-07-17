# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	a=[]
	n=abs(n)
	n=str(n)
	for i in n:
		a.append(int(i))
	for y in range(len(a)-1):
		if a[y]==a[y+1]:
			return True
	return False