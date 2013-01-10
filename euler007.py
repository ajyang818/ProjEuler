# Proj. Euler: #7 - Find the 10,001st prime number

primes = [2, 3, 5]

def isPrime(toTest):
	for i in primes:
		if toTest % i == 0:
			return False
	return True

def tester(numPrime):
	i = 3
	counter = 7
	keepgoing = True

	while keepgoing == True:
		if isPrime(counter) == True:
			i += 1
			primes.append(counter)
			if i == numPrime:
				keepgoing = False
				break
		counter += 2

	return primes[numPrime - 1]

print tester(10001)