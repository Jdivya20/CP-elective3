# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!
def isprime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    return False
def sumOfSquaresOfDigits(n):
    s=0
    while n>=1:
        r=n%10
        s+=r**2
        if n==r==s==1:
            return n
        n=n//10
        if n==0:
            n=s
            s=0
        if n==4:
            return n
def ishappynumber(n):
    # Your code goes here
    if sumOfSquaresOfDigits(n)==1:
        return True
    else:
        return False
# print(sumOfSquaresOfDigits(23))
# print(ishappynumber(1))

def ishappyprimenumber(n):
    # Your code goes here
    if isprime(n) and ishappynumber(n):
        return True
    else:
        return False
print(ishappyprimenumber(23))

# def isPrime(n):
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 return False
#         else:
#             return True
#     return False
            
# def ishappynumber(n):
#     # your code goes here
#     a=[]
#     if n<=0:
#         return False
#     if n==1:
#         return True
#     else:
#         if n<10:
#             n=n**2
#             if n==4:
#                 return False
#         while n>1:
#             if n==4:
#                 return False
#             n=str(n)
#             for i in n:
#                 a.append(int(i)**2)
#             n=sum(a)
#             a=[]
#         return True
# def ishappyprimenumber(n):
#     # Your code goes here
#     if isPrime(n) and ishappynumber(n):
#         return True
#     else:
#         return False
# print(ishappyprimenumber(23))