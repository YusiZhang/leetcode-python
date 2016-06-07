def countPrimes(self, n):
	if n <= 2:
		return 0
	result = [1] * n
	result[0] = result[1] = 0
	for i in xrange(2, n):
		if result[i] == 1:
			for j in xrange(i, (n-1)/i + 1):
				result[i*j] = 0

	return sum(result)