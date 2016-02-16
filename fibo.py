def fibo(limit):


	a = 0
	b = 1
	#a,b = 1,1
	for i in range(limit):
		#a = b
		#b = a + b
		a,b = b,a+b	

	return a

def fibo_list(lt):

	fibo_pos = []
	for i in lt:

		fibo_pos.append(fibo(i))
	
	return fibo_pos	


lt = [1,3,5,99]

print(fibo_list(lt))
		
