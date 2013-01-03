# Euler Problem #4: largest palindrome that's the product of 2 3-digit numbers

test = 123456

def palTester(toTest):
	isPal = True

	if str(toTest)[0] != str(toTest)[-1]: return False
	if str(toTest)[1] != str(toTest)[-2]: return False
	if str(toTest)[2] != str(toTest)[-3]: return False

	return True

def counter():
	high = 100
	highestPal = 1

	for i in range(100,1000):
		for j in range(i,1000):
			# print "i: " + str(i) + ", j: " + str(j)
			count = i * j
			if palTester(count) == True and i*j > highestPal:
				highestPal = i * j
				noteI = i
				noteJ = j
				# print "HIGHESTPAL SWITCHED TO: " + str(i) + "x" + str(j) + " = " + str(i*j)
			# import ipdb; ipdb.set_trace()
			j += 1
		i += 1

	# print "HIGHESTPAL FROM: " + str(noteI) + "x" + str(noteJ) + " = " + str(highestPal)
	return highestPal

print "Highest palindrome: " + str(counter())