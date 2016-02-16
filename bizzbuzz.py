def buzzfizz(num):


	if num % 2 == 0 and num % 3 == 0:
		return 'FizzBuzz'

	elif num % 2 == 0:
		return 'Fizz'

	elif num % 3 == 0:
		return 'Buzz'

	return str(num)

def buzzfizz_list(lt):

	st_lt = []
	for i in lt:
		st_lt.append(buzzfizz(i))

	return st_lt


lt = [1,2,3,4,5,6,7,8,9,10]
print (buzzfizz_list(lt))
		
		

 
