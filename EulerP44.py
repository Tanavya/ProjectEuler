
# 3n^2 - n - 2x = 0

def isPentagonNum(x):

    c = -2*x

    n = (1 + (1 - 12 * c)**0.5)/6

    if n.is_integer():
        return True
    else:
        return False


def pentagon(n):
    return (n*(3*n - 1))/2


def solve():
    A,B = 1,100
    while True:
        for a in range(A,B):
            for b in range(A,B):
                D = abs(pentagon(a) - pentagon(b))
                if isPentagonNum(pentagon(a) + pentagon(b)) and isPentagonNum(D):
                    print pentagon(a), pentagon(b), "D:", D, a, b
                    return D
        A = B
        B *= 10

import time
start = time.time()
ans = solve()
print "Ans:", ans, "found in", time.time() - start, "seconds"