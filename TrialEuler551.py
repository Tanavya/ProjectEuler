#https://www.codechef.com/problems/ALGRIV

import time


def getDigitsSum(n):
    return sum([int(x) for x in str(n)])


def seq(x, START):

    NEXT = START
    yield START
    for i in xrange(10**5, x+1):
        NEXT += getDigitsSum(NEXT)
        yield NEXT, i


for x in seq(10**15, 31054319):
#for x in seq(10, 1):

    print x

