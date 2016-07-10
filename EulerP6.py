"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
#EASYNESS


def SumOfSquares(x):
    sum = 0
    for i in range(x+1):
        sum += i**2

    return sum

def SquareOfSum(x):
    sum = 0
    for i in range(x+1):
        sum += i
    return sum**2


x = 100
print SquareOfSum(x) - SumOfSquares(x)

