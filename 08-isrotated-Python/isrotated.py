# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
	#Your code goes here
	i=0
	s=[]
	while i<len(str1):
		s=str1[1:]+str1[0:1]
		str1=s
		i+=1
		if str1==str2:
			return True
	else:
		return False
print(isrotated("12345", "54321"))