import math

def pyht(maxval):

	pyth_list = []
	for a in range(1,maxval):
		for b in range(a+1,maxval):
			c = math.sqrt(a ** 2 + b ** 2)
			if c > maxval:
				break
			if c == round(c):
				pyth_list.append([a,b,int(c)])

	return sorted(pyth_list)




print(pyht(19))




