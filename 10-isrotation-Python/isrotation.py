# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.
def rightrotate(x,y):
    i=0
    x=str(x)
    while i<len(x):
        x=x[1::]+x[0:1]
        i+=1
        if int(x)==y:
            return True
    return False
def leftrotate(x,y):
    i=0
    x=str(x)
    while i<len(x):
        x=x[-1:]+x[0:-1]
        i+=1
        if int(x)==y:
            return True
    return False
# print(leftrotate(1234,4321))
def isrotation(x, y):
	# Your code goes here
	x=str(x)
	if rightrotate(x,y) or leftrotate(x,y) or x[::-1]==str(y):
		return True
	return False
print(isrotation(3412, 1234))