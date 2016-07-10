
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


def divisibleByAll(n,k):

    for i in range(1,k+1):
        if n % i != 0:
            return False
    return True

def solve():
    num = 1
    for i in range(1,21):
        num *= i

    for n in range(2,21):
        while True:
            if divisibleByAll(num/n, 20):
                num /= n
            else:
                break
    return num

start = time.time()
ans = solve()
print "Ans:", ans, "found in", time.time() - start, "seconds"