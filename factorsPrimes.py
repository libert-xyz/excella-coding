def primes(n):

	c = 0
	for i in range(1,n):

		if n % i == 0:
			c = c + 1
		if c > 2:
			return False	
			break
	return True
	

def divisor(n):
	factors_list = []
	div = 0
	if n == 2:
		factors_list.append(2)
	else:
		for i in range(2,n-1):
			if n % i == 0:
				factors_list.append(i)
				div = n / i
				if div % i == 0:
					factors_list.append(i)
		if len(factors_list) == 0:
			factors_list.append(n)
		
	return factors_list


def factors(n):	
	factors_list = []
	div = n
	i = 0
	divisors = divisor(n)
	if len(divisors) == 1:
		factors_list.append(divisors[i])
	else:
		while div > 1:
			div = div // divisors[i]
			if primes(divisors[i]):
				factors_list.append(divisors[i])
				i = i + 1
			else:
				i = i + 1
	return factors_list
		
def api_factors(lt):
	api_list = []
	for i in lt:
		api_list.append(factors(i)) 
	return api_list

lt = [0, 6, 7, 9,10,102]
print(api_factors(lt))
