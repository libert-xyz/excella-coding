def prime(num):
	c = 0
	
	for i in range(1,num+1):
		
		if num % i == 0:
			c = c + 1

		if c == 3:
			return False
			break
	return True


def gen_primes(x):

	prime_list = []
	for i in range(2,x+1):
		if prime(i):
			prime_list.append(i)

	return prime_list
		

def sexy_primes(num):
	#sexy_lt = []
	#main_lt = []
	primes = gen_primes(num)
	#for i in primes:
	#	if i + 6 in primes and i+6 < num:
	#		sexy_lt.extend((i,i+6))
	#		main_lt.append(sexy_lt)	
	#return main_lt
	return [[i,i+6] for i in primes if i + 6 in primes]
num = 50

print (sexy_primes(num))


			

		
	



	
		
	
		
