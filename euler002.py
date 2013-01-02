# Euler Problem 2: sum of even Fibonacci numbers while numbers in sequence < 4,000,000

i = []
i.append(1)
i.append(2)

n = 2
counter = i[1]

while True:
	i.append(i[n-2] + i[n-1])
	if i[n] > 4000000:
		break
	else:
		if i[n] % 2 == 0:
			counter += i[n]
		n += 1

print counter