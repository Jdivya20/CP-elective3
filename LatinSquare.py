# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(lst):
    # Your code goes here...
    a=[]
    row=len(lst)
    col=len(lst[0])
    print(len(set(lst[0])))
    if row==col:
        for i in lst:
            if len(set(i))!=row:
                return False
            elif len(set(i))==row:
                for j in i:
                    a.append(j)
                if len(set(a))!=col:
                    return False
                
                    a=[]
    return True
print(isLatinSquare([  [ 1, 2, 3, 4 ],
             [ 2, 1, 4, 3 ],
             [ 3, 4, 1, 2 ],
             [ 4, 3, 2, 1 ] ]))
