# Euler Problem 3: largest prime factor of 600,851,475,143

# To fix: handling squares

toBreak = 600851475143
primes = [2, 3]

def findNextPrime(n, toBreak):
    n += 1
    isnPrime = False

    while n <= toBreak:
        for i in primes:
            if n % i == 0:
                isNPrime = False
        else:
            isnPrime = True
            primes.append(n)
            return n
        n += 1

    return n


def breakDown(n, toBreak):

    if toBreak % n == 0 and n != toBreak:
        print "Broke down: " + str(toBreak) + " to " + str(toBreak/n)
        breakDown(n, toBreak/n)
        # return "Returning: " + str(toBreak / n)
        return toBreak / n
    # return "Returning: " + str(toBreak)
    return toBreak



n = 2
# toBreak = 8
while n < toBreak:
    toBreak = breakDown(n, toBreak)
    n = findNextPrime(n, toBreak)

print "Highest prime factor: " + str(n)


# findAllPrimes(toBreak)
# print breakDown(toBreak)