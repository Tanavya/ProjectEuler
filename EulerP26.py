
from decimal import *
import re

def getSubStrings(L, n, x):

    substrings = []
    i = 0
    while i <= x + 1:
        substrings.append(L[i:i+n])
        i += n

    return substrings
def displaymatch(match):
    if match is None:
        return 0

    return len(match.group(1))

getcontext().prec = 2000
MAX = 6
for i in xrange(11,1000):
    x = Decimal(1.0)/Decimal(i)
    #x = str(x).replace("0.00", "").replace("0.0", "")[:-1]
    pattern = re.search(r"^[0-9]\.[0-9]*([0-9]{7,}?)(\1+)[0-9]*?$", str(x))

    length = displaymatch(pattern)
    #print length
    if length > MAX:
        MAX = i


    #print x,i

print MAX, "max"

def recurring_cycle(n, d):
    # solve 10^s % d == 10^(s+t) % d
    # where t is length and s is start
    for t in range(1, d):
        if 1 == 10**t % d:
            return t
    return 0

longest = max(recurring_cycle(1, i) for i in range(2,1001))
print([i for i in range(2,1001) if recurring_cycle(1, i) == longest][0])


d = 20


def period(d):
    while d % 2 == 0: d /= 2
    while d % 5 == 0: d /= 2

    p = 1
    for p in range(1, d):
        if (10**p - 1) % d == 0:
            return p
    return p


print period(983)