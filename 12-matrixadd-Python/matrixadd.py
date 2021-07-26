# matrixAdd(L, M)[10 pts]
# Background: we can think of a 2d list in Python as a matrix in math. To add two matrices, L and M, they must have 
# the same dimensions. 
# Then, we loop over each row and col, and the result[row][col] is just the sum of L[row][col] and M[row][col]. For example:
# L = [ [1,  2,  3],
#       [4,  5,  6] ]
# M = [ [21, 22, 23],
#       [24, 25, 26]]
# N = [ [1+21, 2+22, 3+23],
#       [4+24, 5+25, 6+26]]
# assert(matrixAdd(L, M) == N)
# With this in mind, write the function matrixAdd(L, M) that takes two rectangular 2d lists (that we will consider 
# to be matrices) that you 
# may assume only contain numbers, and returns a new 2d list that is the result of adding the two matrices. Return 
# None if the two matrices 
# cannot be added because they are of different dimensions.

def matrixadd(L, M):
	# Your code goes here
	row=len(L)
	col=len(L[0])
	result=[]
	for y in range(row):
		result+=[[0]*col]
	if len(L)!=len(M) or len(L[0])!=len(M[0]):
		return None
	x=0
	while x<len(M)-1:
		if len(M[x])!=len(M[x+1]):
			return None
		x+=1
	for i in range(row):
		for j in range(col):
			result[i][j]=L[i][j]+M[i][j]
	return result
print(matrixadd([[1,2,3],
    [4 ,5,6],
    [7 ,8,9]], [[9,8,7],
    [6,5,4],
    [3,2,1]]))