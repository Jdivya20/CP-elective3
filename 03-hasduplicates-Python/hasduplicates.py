# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	# Your code goes here
	a=[]
	for i in L:
		for j in i:
			if j in a:
				return True
			if j not in a:
				a.append(j)
	return False
print(hasduplicates([[2, 7, 9], [9, 5, 1], [4, 3, 8]]))