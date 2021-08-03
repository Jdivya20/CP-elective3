# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	# Your code goes here
	n=abs(n)
	a=[]
	l=[]
	m=[]
	e=[]   
	b=[]
	count=1
	v=0
	for i in str(n):
		a.append(int(i))
	for x in range(len(a)-1):
		if a[x]!=a[x+1] and x<=len(a)-1:
			l.append((a[x],count))
			count=1
		else:
			count+=1
	print(x+1)
	print(len(a)-1)
	if x+1==len(a)-1:
		if a[x]==a[x+1]:
			l.append((a[x],count))
		elif a[x]!=a[x+1]:
			l.append((a[x+1],count))
	for o in l:
		m.append(o[1])
	z=0
	for s in m:
		if s>=z:
			z=s
	b.append(z)
	for p in l:
		for w in b:
			if p[1]==w:
				e.append(p[0])
	if len(e)==1:
		return max(e)
	else:
		return min(e)

print(longestdigitrun(123330001))