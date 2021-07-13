# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	n1=abs(n)
	a=[]
	s=''
	for i in str(n1):
		a.append(int(i))
	a.reverse()
	if k>=len(a):
		a.append(d)
	else:
		a[k]=d
	# print(reversed(a))
	for i in a[::-1]:
		s=s+str(i)
	b=int(s)
	if n<0:
		return(-abs(b))
	else:
		return(b)

