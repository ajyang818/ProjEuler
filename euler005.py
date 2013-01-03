# Euler Prob #5: smallest positive number that's evenly divisible by all numbers between 1 and 20

runningFactors = [2, 3]

def findFactors(base):
	while base != 1:
		for i in runningFactors:
			if base % i == 0:
				base = base / i
		runningFactors.append(base) 
	return

def caller(maxNum):
	for j in range(4, maxNum):
		findFactors(j)
	return

def answer():
	result = 1
	for i in runningFactors:
		result = result * i
	return result

caller(20)
print "Smallest common multiple is: " + str(answer())