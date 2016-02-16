def prime(num):

	c = 0

	for i in range(1,num+1):
		if num % i == 0:
			c = c + 1
			

		if c == 3:
			return False	
			break

	return True


def prime_lt(lt):
	
	prime_list = []
	for i in lt:
		prime_list.append(prime(i))


	return prime_list
	
lt = [2, 3, 4]
print (prime_lt(lt))
