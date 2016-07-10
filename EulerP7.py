"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import math

def isPrime(x):
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x) + 1), 2):
        if x % i == 0:
            return False
    return True


def getPrimes(x):
    i = 1
    while True:
        if isPrime(x):
            yield x, i
            if i == 10001:
                break
            i += 1
        x += 1

    return

for i in getPrimes(2):
    print i

