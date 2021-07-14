# powerSum(n, k) [15 pts]
# Write the function powerSum(n, k) that takes two 
# possibly-negative integers n and k and returns the 
# so-called power sum: Specify the time complexity based 
# on the solution that you have given. [Hint: This can be 
# solved in (n * log k)  or better.

#    1**k + 2**k + ... + n**k

# If n is negative, return 0. Similarly, if k is negative, 
# return 0.

def powerSum(n, k):
    s=0
    # Your code goes here...
    if n<0 or k<0:
        return 0
    else:
        for i in range(1,n+1):
            s=s+i**k
        return s

# Write your own test cases here...

print ("All test cases passed...")