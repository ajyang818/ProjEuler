# Sum of all primes below 2 million

import math

primes = [2]
sum_of_primes = 2
cap = 2000000

i = 3
while i < cap:
    print i
    is_prime = True
    sqrt_cap = math.sqrt(i)

    for prime in primes:
        if prime > sqrt_cap:
            is_prime = True
            break
        if i % prime == 0:
            is_prime = False
            break

    if is_prime == True:
        primes.append(i)
        sum_of_primes += i
    i += 2

print sum_of_primes