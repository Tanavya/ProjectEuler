import time
import random

"""
x = [random.randint(10**12, 10**13) for i in range(10)]
s = 0
for e in x:
    print e, e%10**4
    s +=  e%10**4

print int(str(s)[-4:]), int(str(sum(x))[-4:])
#print str(random.random()).replace(".", "")
"""

def solve1():
    s = 0
    for p in range(1,1001):
        s += p**p

    return str(s)[-10:]

#^ this is a nooby method, prolly only work in few langs like Python... Here's for a more smart one.

def solve2():
    s = 0
    for p in range(1,1001):
        s += p**p % 10**10

    return s % 10**10

start = time.time()
ans = solve1()
print "Ans1:", ans, "found in", time.time() - start, "seconds"

start = time.time()
ans = solve2()
print "Ans2:", ans, "found in", time.time() - start, "seconds"