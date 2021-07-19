# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.
def coladd(a):
	row=len(a)
	col=len(a[0])
	b=[]
	for i in range(row):
		s=0
		for j in range(col):
			s+=a[j][i]
		b.append(s)
	return b
    # c=sum(b)
    # print(b)
def isdiag(a):
    row=len(a)
    col=len(a[0])
    b=[]
    s=0
    for i in range(row):
        
        for j in range(col):
            if i==j:
                s+=a[i][j]
                b.append(s)
        return b
print(coladd([[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12],[4, 15, 14, 1]]))
def ismostlymagicsquare(a):
	# Your code goes here
	b=[]
	for j in a:
		b.append(sum(j))
	for i in b:
		if b.count(i)==len(b) and coladd(a)==b and isdiag(a):
			return True
		else:
			return False
print(ismostlymagicsquare([[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12],[4, 15, 14, 1]]))