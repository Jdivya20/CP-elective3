# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).
def pronic(n):
	return n*(n+1)
def nthpronicnumber(n):
	# Your code goes here
	num=0
	count=0
	while count<=n:
		num+=1
		if pronic(num):
			count+=1
	return pronic(n)