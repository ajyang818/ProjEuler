# Proj. Euler #6: Difference between sum of squares and square of sum of 1-100

def sumOfSquares(min, max):
    runningSum = 0
    for i in range(min, max+1):
        runningSum += (i * i)

    return runningSum

def squareOfSum(min, max):
    runningSum = 0
    for i in range(min, max+1):
        runningSum += i

    return runningSum * runningSum

def findDiff(min, max):
    return squareOfSum(min, max) - sumOfSquares(min, max)

print findDiff(1, 100)