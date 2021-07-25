# Write the function fun_nth_palindromic_prime(n) that takes 
# a non-negative int n and returns the nth palindromic Prime, 
# which is a palidrome number such that 
# it is also a prime. 

# For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) 
# returns 2
def isprime(n):
	if n>1:
		for i in range(2,n):
			if n%i==0:
				return False
		else:
			return True
	else:
		return False
def ispalindrome(n):
	n=str(n)
	if n==n[::-1]:
		return True
	return False
def fun_nth_palindromic_prime(n):
	count=0
	num=0
	while count<=n:
		num+=1
		if isprime(num) and ispalindrome(num):
			count+=1
	return num