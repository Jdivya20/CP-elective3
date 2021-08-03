# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).
def isprime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
def circularprime(n):
    a=str(n)
    a=a[::-1]
    a=int(a)
    if isprime(n) and isprime(a):
        return True
    else:
        return False
print(circularprime(27))
def nthcircularprime(n):
	# Your code goes here
	count=0
	num=0
	while count<n:
		num+=1
		if circularprime(num):
			count+=1
	return num
print(nthcircularprime(0))