# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    row=len(m1)
    col=len(m2[0])
    result=[]
    for x in range(row):
        result+=[[0]*col]
    if len(m1[0])!=len(m2):
        return None
    for i in range(row):
        for j in range(col):
            for k in range(len(m2)):
                result[i][j]+=m1[i][k]*m2[k][j]
    return result
print(fun_matrixmultiply([[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]], [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]))



