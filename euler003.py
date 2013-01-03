# Euler Problem 3: largest prime factor of 600,851,475,143

from math import sqrt

toBreak = 600851475143001
primes = [2, 3]

def countNCheck(toBreak):
    n = 5
    highestPrime = 1
    orig = toBreak

    if toBreak % 2 == 0: 
        toBreak = toBreak / 2
        highestPrime = 2
    if toBreak % 3 == 0: 
        toBreak = toBreak / 3
        highestPrime = 3

    while n <= toBreak and n <= sqrt(orig):
        # print "n is at: " + str(n) + "; toBreak is at: " + str(toBreak)
        isNPrime = True
        for i in primes:
            if n % i == 0:
                isNPrime = False
                # print str(n) + " is not prime"
        if isNPrime == True:
            primes.append(n)
            if toBreak % n == 0: 
                toBreak = toBreak / n
                # print "Broke down: " + str(toBreak) + " to " + str(toBreak/n)
                highestPrime = n
        n += 2

    # import ipdb; ipdb.set_trace()
    return highestPrime

toBreak = 125
print "Highest prime factor is: " + str(countNCheck(toBreak))
