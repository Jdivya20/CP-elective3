# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.



def fun_nearestbusstop(street):
	b=[]
	for i in range(0,11):
		a=8*i
		b.append(a)
	for j in range(len(b)-1):
		if street in b:
			return(street)
		elif b[j]<street<b[j+1] and abs(b[j]-street)==abs(b[j+1]-street):
			return(b[j])
		elif b[j]<street<b[j+1] and abs(b[j]-street)<abs(b[j+1]-street):
			return(b[j])
		elif b[j]<street<b[j+1] and abs(b[j]-street)>abs(b[j+1]-street):
			return(b[j+1])
