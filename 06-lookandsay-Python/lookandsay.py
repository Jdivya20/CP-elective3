# Write the function lookAndSay(a) that takes a list of numbers and returns a list of numbers
# that results from "reading off" the initial list using the look-and-say method, using tuples 
# for each (count, value) pair.
# 
# For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

def lookandsay(a):
	# Your code goes here
	# d={}
	# b=[]
	# for i in a:
	# 	if i in d:
	# 		d[i]=d[i]+1
	# 	else:
	# 		d[i]=1
	# for each in d.items():
	# 	b.append(each[::-1])
	# return b
	count=0
	x=0
	temp=[]
	for i in a:
		if i==x:
			count+=1
		else:
			temp.append((count,x))
			x=i
			count=1
	temp.append((count,x))
	return temp[1:]
print(lookandsay([1,1,1]))