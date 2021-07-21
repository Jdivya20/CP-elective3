# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).
def isPrime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True
    return False
            
def ishappynumber(n):
    # your code goes here
    a=[]
    if n<=0:
        return False
    if n==1:
        return True
    else:
        if n<10:
            n=n**2
            if n==4:
                return False
        while n>1:
            if n==4:
                return False
            n=str(n)
            for i in n:
                a.append(int(i)**2)
            n=sum(a)
            a=[]
        return True


def fun_nth_happy_prime(n):
	num=0
	count=0
	while count<=n:
		num+=1
		if isPrime(num) and ishappynumber(num):
			count+=1
		
	return num
print(fun_nth_happy_prime(0))