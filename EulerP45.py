import time

def isPentagonNum(x):

    c = -2*x

    n = (1 + (1 - 12 * c)**0.5)/6

    if n.is_integer():
        return True
    else:
        return False

def isTriangularNum(x):

    n = (-1 + (1+8*x) ** 0.5)/2

    if n.is_integer():
        return True
    else:
        return False

def HexagonNum(n):
    return n*(2*n-1)

def solve():
    n = 144
    while True:
        h = HexagonNum(n)
        if isTriangularNum(h) and isPentagonNum(h):
            return h
        n += 1

start = time.time()
ans = solve()
print "Ans:", ans, "found in", time.time() - start, "seconds"