# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22
def isprime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True
    return False
def smithnumber(n):
    a=''
    b=[]
    o=[]
    i=0
    l=str(n)
    while i<=n:
        if isprime(i) and n%i==0:
            a+=str(i)
            n=n//i
            i=0
        i+=1
    # i=0
    # n=str(n)
    for x in l:
        b.append(int(x))
    for k in a:
        o.append(int(k))
    if sum(o)==sum(b) and int(a)!=int(l):
        return True
    else:
        return False
# print(smithnumber(4))

def fun_nth_smithnumber(n):
    num=0
    count=0
    while count<=n:
        num+=1
        if smithnumber(num):
            count+=1
    return num
print(fun_nth_smithnumber(1))