# Write the function nthCarolPrime(n), which takes a non-negative int and returns the nth Carol Prime, 
# which is a prime number of the form ((2**k - 1)**2 - 2) for some value positive int k. For example, 
# if k equals 3, ((2**3 - 1)**2 -2) equals 47, which is prime, and so 47 is a Carol Prime. 
# The first several Carol primes are: 7, 47, 223, 959, 3967, 16127, 65023, 261119, 1046527,... As such, 
# nthCarolPrime(0) returns 7.
# Note: You must use a reasonably efficient approach that quickly works up to n==9, which 
# will return a 12-digit answer! In particular, this means you cannot just edit isPrime. 
# Hint: you may need to generate only Carol numbers, and then test those as you go 
# for primality (and you may need to think about that hint for a while for it to make sense!).

def isprime(n):
    if n>1:
        for i in range(2,n):
            if n%2==0:
                return False
        else:
            return True
    else:
        return False
def carolprime(k):
    carol=((2**k - 1)**2 - 2)
    if isprime(carol):
        return carol
def fun_nth_carolprime(n):
    count=0
    num=0
    while count<=n:
        num+=1
        if carolprime(num):
            count+=1
    return carolprime(num)
print(fun_nth_carolprime(0))
print(fun_nth_carolprime(1))