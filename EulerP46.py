
import time

def isPrime(n):

    if n == 1:
        return False

    if n == 2 or n == 3:
        return True

    elif n % 2 != 0 and n % 3 != 0:

        for curr in range(3, int(n**0.5) + 1, 2):
            if n % curr == 0:
                return False
        return True

    else:
        return False

def isConjectureTrue(N):
    """
    n = N
    s = 1
    while True:
        n -= 2
        if n <= 0:
            return False
        if isPrime(n):
            while n + 2 * (s**2) <= N:
                if n + 2 * (s**2) == N:
                    return True
                else:
                    s += 1

    """
    SqBase = 1
    while True:
        double_square = 2*SqBase**2
        if N-double_square < 0:
            return False
        if isPrime(N-double_square):
            return True
        SqBase += 1

    return False


def solve():
    N = 33
    while True:
        if not isConjectureTrue(N):
            return N
        while True:
            N += 2
            if not isPrime(N):
                break


start = time.time()
ans = solve()
print "Ans:", ans, "found in", time.time() - start, "seconds"