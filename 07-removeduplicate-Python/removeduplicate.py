# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.

def removeduplicate(text):
	# Your code goes here
	a=[]
	b=[]
	for i in text:
		a.append(i)
	for i in a:
		if i not in b:
			b.append(i)
	return "".join(b)