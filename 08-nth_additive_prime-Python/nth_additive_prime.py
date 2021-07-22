# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

def isprime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
def isadditiveprime(n):
    s=0
    if isprime(n):
        while n>0:
            r=n%10
            n=n//10
            s+=r
        if isprime(s):
            return True
    return False
print(isadditiveprime(9))


def fun_nth_additive_prime(n):
	num=0
	count=0
	while count<=n:
		num+=1
		if isadditiveprime(num):
			count+=1
	return num
print(fun_nth_additive_prime(0))