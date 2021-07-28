# canQueenAttack(qX, qY, oX, oY) [15 pts]
# Given the position of the queen (qX, qY) and the opponent (oX, oY) on a chessboard. The task is to determine 
# whether the queen can attack the opponent or not. Note that the queen can attack in the same row, same column and 
# diagonally.

def canqueenattack(qR, qC, oR, oC):
	# Your code goes here
	if oC == qC:
		 return True
	if oR == qR:
		return True
	a=abs(qR - oR)
	b=abs(qC - oC)
	if b == a:
		return True
	return False
print(canqueenattack(4, 5, 6, 7))