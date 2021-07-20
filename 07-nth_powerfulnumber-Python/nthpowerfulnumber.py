# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.
import math
def isPowerful(n):
	i=1
	while(i<=n):
	# for i in range(1,n):
	# m=a**2*b**3
	# ==> a=sqrt(m/b**3)
		num=math.sqrt(n/i**3)
		if(num == int(num)):
			return True
		i=i+1
	else:
		return False
def nthpowerfulnumber(n):
	# Your code goes here
	count = 0
	number = 0
	while(count <= n):
		number=number+1
		if(isPowerful(number)):
			count+=1
	return number
print(nthpowerfulnumber(1))
print(nthpowerfulnumber(12))
# def isprime(n):
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 return False
#         else:
#             return True
#     else:
#         return False
# # print(isprime(2))
# def ispowerful(n):
# 	a=[]
# 	i=1
# 	if n==1:
# 		return True
# 	while(i<=n):
# 	# for i in range(1,n):
# 		if n%i==0 and isprime(i):
# 			a.append(i)
# 		i=i+1
# 	# return lis
# 	# print(lis)
# 	for i in range(len(a)-1):
# 		if n==(a[i]**2)*(a[i+1]**3)or n==(a[i]**3)*(a[i+1]**2):
# 		# if n%(i**2)==0:
# 			return True
# 	else:
# 		return False
# print(ispowerful(12))
# # print(1%1)
# # def nthpowerful(n):
# #     count = 0
# #     number = 0
# #     while(count <= n):
# #         number=number+1
# #         if(ispowerful(number)):
# #             count+=1
# #     return number
# # print(nthpowerful(1))

