# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46
def istidy(n):
    n=str(n)
    a=[]
    for i in n:
        a.append(int(i))
    if a== sorted(a):
        return True
    return False
# print(istidy(1156))
def fun_nth_tidynumber(n):
    num=0
    count=0
    while count<=n:
        num+=1
        if istidy(num):
            count+=1
    return num
print(fun_nth_tidynumber(35))