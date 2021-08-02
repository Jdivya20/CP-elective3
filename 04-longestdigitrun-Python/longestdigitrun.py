# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	# Your code goes here
	n=abs(n)
	next_num=1
	flag=1
	temp=0
	count=0
	while(n>0):
		first=n%10
		if(first!=next_num):
			count=1
		n=n//10
		if(next_num == first):
			count+=1
			# return True
		next_num=first
		if(count>temp):
			temp=count
			flag=next_num
		if(temp==count):
			if(flag>next_num):
				flag=next_num
	return flag
print(longestdigitrun(-677886))