# Proj. Euler #9 - Special Pythagorean Triplet where the three numbers sum to 1000

def isPyTriplet(numbers):
	c = sorted(numbers)[-1]
	a = sorted(numbers)[0]
	b = sorted(numbers)[1]

	if (a*a) + (b*b) == (c*c): return True
	return False

def cycler(max):
	for a in range(1, max):
		for b in range(a, max):
			for c in range(b, a+b):
				print [a, b, c]
				if a + b > c and a + c > b and b + c > a:
					if isPyTriplet([a, b, c]) and a + b + c == max:
						return a * b * c

	return None

print cycler(1000)