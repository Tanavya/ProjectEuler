
import time

def solve():
    """
    m = 0
    for a in range(1,100):
        for b in range(1,100):
            x = a**b
            s = sum([int(i) for i in str(x)])
            if s > m:
                m = s
    return m
    """

    return max([sum([int(i) for i in str(a**b)]) for a in range(1,100) for b in range(1,100)])



start = time.time()
ans = solve()
print "Ans:", ans, "found in", time.time()-start, "seconds"
