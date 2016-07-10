"""Let a0, a1, a2, ... be an integer sequence defined by:

a0 = 1;
for n > 1, an is the sum of the digits of all preceding terms.
The sequence starts with 1, 1, 2, 4, 8, 16, 23, 28, 38, 49, ...
You are given a106 = 31054319.

Find a1015.

"""


def getDigitsSum(x):
    sum = 0
    while x:
        sum += x % 10
        x /= 10

    return sum


def seq(x):
    NEXT = 1
    s = [NEXT]
    print NEXT, 1, NEXT % 9
    for i in xrange(2,x):
        NEXT += getDigitsSum(NEXT)
        print NEXT,  NEXT/9, NEXT % 9 , "    ", i
        s.append(NEXT)

    return s


def seq2(x):
    NEXT = 1
    s = [NEXT]
    #print NEXT, 1, NEXT % 9
    for i in xrange(2,x):
        NEXT += getDigitsSum(NEXT)
        #print NEXT,  NEXT/9, NEXT % 9 , "    ", i
        s.append(NEXT)

    return s

#for i in seq(10**15): print i
print seq(100)
print "\n" * 5

print seq(100)
x = [1,2,4,8,7,5]
N = 0
n = x[(N+6)%6]




for i in range(100):
    x = [1,2,4,8,7,5]
    if i % 9 in x:
        if i in seq2(100):
            print i, "init"
        else:
            print i


#0,0,2,4,4,2,6,6,8,4,4,8

#print sum(getDigits(52))

