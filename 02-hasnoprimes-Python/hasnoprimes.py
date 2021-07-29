# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.

def isprime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
def fun_hasnoprimes(l):
	for i in l:
		for j in range(len(i)):
			if isprime(i[j]):
				return False
	return True
print(fun_hasnoprimes([[2]]))

