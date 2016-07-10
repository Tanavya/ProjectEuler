import itertools
import time

start = time.time()
primes = [2,3,5,7,11,13,17]

num = "0123456789"

perms =  [ "".join(x) for x in itertools.permutations(num)]


def subStringDivisible(n):
    if int(n[3]) % 2 != 0:
        return False
    for i in range(1,8):
        if int(n[i:i+3]) % primes[i-1] != 0:
            return False
    return True

SUM = 0
for n in perms:
    if subStringDivisible(n):
        SUM += int(n)

print "Ans:", SUM, "found in", time.time()-start, "seconds"



