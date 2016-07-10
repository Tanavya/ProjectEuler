import time


import itertools

def isPrime(n):

    if n == 2 or n == 3:
        return True

    elif n > 2 and n % 2 != 0 and n % 3 != 0:

        for current in range(5, int(n**0.5)):
            if n % current == 0:
                return False
        return True

    else:
        return False


def solve():
    for l in range(7,5, -1):

        pan = "123456789"[:l]

        perms =  sorted([ "".join(x) for x in itertools.permutations(pan)], reverse=True)

        for perm in perms:
            if isPrime(int(perm)):
                return perm

start = time.time()
ans = solve()
print "Ans:", ans, "found in", time.time() - start, "seconds"