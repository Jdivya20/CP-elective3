# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	d={}
	e=[]
	a=[]
	f=[]
	for x in str(n):
		a.append(int(x))
	for i in a:
		if i in d:
			# d[i]=d[i]+1
			d[i]=a.count(i)
			# print(mode.count(i))
		else:
			d[i]=1
	s=1000
	c=list(sorted(d.values()))
	if len(a)==1:
		return a[0]
	else:
		for j in range(len(c)-1):
			if c[j]==c[j+1] and c[j]<=s:
				s=c[j]
		for key,values in d.items():
			if values==s:
				e.append(key)
				f.append(values)
		if len(d)==len(e) or min(f)==max(f) and max(c)==max(f):
			return(min(e))
		return(max(d,key=d.get))