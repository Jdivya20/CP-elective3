# Write the function alternatingSum(a) that takes a list of numbers and returns the 
# alternating sum (where the sign alternates from positive to negative or vice versa). 
# For example, alternatingSum([5,3,8,4]) returns 6 (that is, 5-3+8-4). If the list is empty, return 0.




def fun_alternatingsum(a):
    even=[]
    odd=[]
    even=a[::2]
    for i in range(len(a)):
        if i%2!=0:
            odd.append(a[i])
    return sum(even)-sum(odd)
print(fun_alternatingsum([]))


