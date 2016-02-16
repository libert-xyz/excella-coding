def sqrSum(num):

	suma = 0
	numstr = str(num)
	for i in range(len(numstr)):
		suma = suma + ( int(numstr[i]) * int(numstr[i]) )

	return suma


def sqr_api(lt):

	sqr_lt = []
	for i in lt:
		sqr_lt.append(sqrSum(i))

	return sqr_lt

lt = [40,27,987]

print (sqr_api(lt))

