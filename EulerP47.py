"""
The first two consecutive numbers to have two distinct prime factors are:


14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
"""
import time

def PrimeFactors(n):

    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)

    d = 3
    while d*d <= n:

        while n % d == 0:
            n /= d
            factors.append(d)

        d += 2

    if n > 1:
        factors.append(n)

    return factors

nums = range(2,1000)
def solve(n):

    nums = range(2,n)

    for i in range(len(nums)-3):
        a = set(PrimeFactors(nums[i]))
        b = set(PrimeFactors(nums[i+1]))
        c = set(PrimeFactors(nums[i+2]))
        d = set(PrimeFactors(nums[i+3]))

        if len(a) == len(b) == len(c) == len(d) == 4:
            return nums[i]

    return solve(n*10)

start = time.time()
ans = solve(1000)
print "Ans:", ans, "found in", time.time() - start, "seconds"