# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.
def automorphic(n):
	sqr=n**2
	rem=sqr%10
	if rem==n:
		return True
	else:
		return False
def nthautomorphicnumbers(n):
	# Your code goes here
	num=0
	count=0
	while count<=n:
		num+=1
		if automorphic(num):
			count+=1
		
	return num
	