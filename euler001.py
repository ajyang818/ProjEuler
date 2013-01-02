# Euler Project #1: sum of all multiples of 3 or 5 below 1000

counter = 0

for i in range(0,1000):
	toggle = False

	if i % 3 == 0:
		toggle = True
	elif i % 5 == 0:
		toggle = True
	else:
		toggle = False

	if toggle == True:
		counter += i

print counter