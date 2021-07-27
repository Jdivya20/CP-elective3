# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.


# def revRecur(n,ro=0):
#     if n//10==0:
#         return (ro*10)+n
#     else:
#         return revRecur(n//10,(10*ro)+(n%10))

# global_list = []
# def get_numbers(input_num, temp_list):
#     remainder = input_num%10
#     rem_num = int(input_num/10)
#     if remainder%2 ==0:
#         temp_list.append(remainder)
#     if rem_num:
#         get_numbers(rem_num, temp_list)
# def convert_list_to_number(nums, base=10):
#     if len(nums) == 1:
#         return nums[0]
#     else:
#         return nums[-1] + base * convert_list_to_number(nums[:-1], base)
# def fun_recursion_onlyevendigits(l):
#     temp_list = []
#     if not (len(l) == 0):
#         get_numbers(revRecur(l[0]), temp_list)
#         if temp_list:        
#             tmp = convert_list_to_number(temp_list)
#             global_list.append(tmp)
#         else:
#             global_list.append(0)
        
#         return fun_recursion_onlyevendigits(l[1:])
#     return global_list
# print(fun_recursion_onlyevendigits([]))
# print(fun_recursion_onlyevendigits([332, 81, 11]))


def getEvenDigits(n,i=0,x=0):
    if(n == 0):
        return x
    else:
        rem = n%10
        if(rem % 2 == 0):
            x += rem*(10**(i))
            i+=1 
        return getEvenDigits(n//10,i,x)
        
def onlyEvenDigitsHelper(l,res=[]):
    if(l == []):
        return res
    else:
        res.append(getEvenDigits(l[0]))
        return onlyEvenDigitsHelper(l[1:],res)
def fun_recursion_onlyevendigits(l):
    if(l == []):
        return []
    return onlyEvenDigitsHelper(l,[])
print(fun_recursion_onlyevendigits([]))
print(fun_recursion_onlyevendigits([332, 81, 11]))