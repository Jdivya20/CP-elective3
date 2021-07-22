# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



def fun_interleave(s1,s2):
	a=[]
	b=[]
	s=[]
	for i in s1:
		a.append(i)
	for j in s2:
		b.append(j)
	x=0
	if len(s1)==len(s2):
		while x<len(s2):
			s+=a[0:1]+b[0:1]
			a.pop(0)
			b.pop(0)
			x+=1
		return (''.join(s))
	elif len(s1)<len(s2):
		while x<len(s1):
			s+=a[0:1]+b[0:1]
			a.pop(0)
			b.pop(0)
			x+=1
		s+=b[::]
		return (''.join(s))
	elif len(s2)<len(s1):
		while x<len(s2):
			s+=a[0:1]+b[0:1]
			a.pop(0)
			b.pop(0)
			x+=1
		s+=a[::]
		return (''.join(s))
print(fun_interleave('pto', 'yhn'))
print(fun_interleave('a#', 'cD!f2'))
	