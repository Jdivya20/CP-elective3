# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.
def property309(n):
	res=n**5
	a=[]
	for i in str(res):
		a.append(int(i))
	for x in range(0,10):
		if x not in a:
			return False
	return True
def nthwithproperty309(n):
	# Your code goes here
	num=0
	count=0
	while count<=n:
		num+=1
		if property309(num):
			count+=1
		
	return num
print(nthwithproperty309(0))