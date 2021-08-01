# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.


def fun_carrylessadd(x, y):
	if x==0 or y==0:
		return x+y
	elif x+y< 10:
		return x+y
	elif x<10 or y<10:
		s=(x+y)-10
		return s
	else:
		s=''
		# for i in range(len(x)-1):
		while x>10 and y>10:
			
			r1=x%10
			r2=y%10
			s1=r1+r2
			s+=str(s1-10)
			x=x//10
			y=y//10
	s=s[::-1]
	return int(s)
print(fun_carrylessadd(121, 0))

