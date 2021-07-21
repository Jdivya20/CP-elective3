# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)

def ishappynumber(n):
	# your code goes here
	a=[]
	if n<=0:
		return False
	if n==1:
		return True
	else:
		if n<10:
			n=n**2
			if n==4:
				return False
		while n>1:
			if n==4:
				return False
			n=str(n)
			for i in n:
				a.append(int(i)**2)
			n=sum(a)
			a=[]
		return True
print(ishappynumber(98))
def nth_happy_number(n):
	num=0
	count=0
	while count<n:
		num+=1
		if ishappynumber(num):
			count+=1
		
	return num
