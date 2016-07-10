
from math import factorial
import time
def ncr(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))


def solve():
    count = 0
    for n in range(23,101):
        for r in range(4,n):
            if ncr(n,r) > 1000000:
                count += 1
    return count

start = time.time()
ans = solve()
print "Ans:", ans, "found in", time.time()-start, "seconds"