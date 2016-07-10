


def findSums( end):

    Q = [[]]
    perms = set([])
    while Q:

        currPerm = Q.pop(0)


        #print currPerm
        if sum(currPerm) == end:
            perms.add(tuple(currPerm))



        moves = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0]

        for move in moves:

            newPerm = currPerm[:]
            newPerm.append(move)

            if sum(newPerm) <= 2 and set(newPerm) not in [set(p) for p in Q]:
                Q.append(newPerm)

    return perms
"""
f = findSums(2)
for p in f:
    print sorted(p)
"""

coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0]

"""
perms = set([])
def check(x):
    if sum(x) == 2 and set(x) not in [set(p) for p in perms] :
        perms.add(tuple(x))
    return perms


c = [[0][:] for i in range(5)]
for c[0] in coins:
    check([c[0]])
    for c[1] in coins:
        check(c[:2][:])
        for c[2] in coins:
            check(c[:2][:])
            for c[3] in coins:
                check(c[:3])
                for c[4] in coins:
                    check(c[:])


for perm in perms:
    print perm

print len(perms)

coins = [0] * 8 + [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0]
perms = set() # invariant no repeated elements,

#from itertools import *
# return elements with length=5 repeat

def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    print pool, "poop"
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    print "indi", indices
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)
"""
"""
for x in combinations_with_replacement(coins,10):
    print x

"""
"""
for comb in combinations:
    for x in permutations(comb):
        if sum(x) == 2:
            perms.add(x)

for p in perms: print p
"""
"""
for i in range(5):
    for j in range(5):
        for I in range(5):
            for J in range(5):
                if i + j + I + J == 13:
                    print i, j, I, J

"""
"""
x = coins[:]
P = []
def r(n, L):

    for i in x:
        if sum(L) > 2:
            return
        if n <= 3:
            r(n+1, L + [i])

    P.append(L)

r(0, [])
l = set([])
P = [sorted(p) for p in P if sum(p) == 2]
print len(P), P

X = set(tuple(p) for p in P)
for p in X:
    print list(p), "1"

"""


'''x = coins[:]
P = []
def r(n, L, t, F):

    for i in x:
        if sum(L) > F or (n >= t and sum(L) < 0.5):
            return
        #if set(L) in [set(p) for p in P]:
        #    break
        if n <= t:
            r(n+1, L + [i], t, F)


    print L
    P.append(L)

r(0, [], 100, 1)

P1 = [sorted(p) for p in P if round(sum(p),2) == 1]
for p in P1:
    print sum(p), p
print len(P1), P1
print "P", P
'''





a1 = [[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2], [0.2, 0.2, 0.2, 0.2, 0.2], [0.1, 0.1, 0.1, 0.1, 0.1, 0.5], [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.1, 0.2, 0.5], [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.02, 0.1, 0.2, 0.5], [0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.1, 0.2, 0.5], [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.05, 0.1, 0.2, 0.5], [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5], [0.01, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.05, 0.1, 0.2, 0.5], [0.05, 0.05, 0.05, 0.05, 0.1, 0.2, 0.5], [0.1, 0.1, 0.1, 0.2, 0.5], [0.1, 0.2, 0.2, 0.5], [0.5, 0.5], [1.0]]

a5 = [[0.2, 0.2, 0.1], [0.1, 0.1, 0.1, 0.1, 0.1]]
a3 = [[0.1, 0.1], [0.2], [0.02] * 10, [0.01] ]

#vals = {1: a1, 0.5: [[0.2, 0.2, 0.1], [0.1, 0.1, 0.1, 0.1, 0.1]]}

vals = {1.0: [[0.5, 0.5]], 0.5: [[0.2, 0.2, 0.1]], 0.2: [[0.1, 0.1]], 0.1: [[0.05, 0.05]], 0.05: [[0.02, 0.02, 0.01]], 0.02: [[0.01, 0.01]] }

#perms = [[0.05]]


def rec(x, perms):
    for i,e in enumerate(x):
        if e != 0.01:
            v = vals[e]
            temp = sorted([a + x[:i] + x[i+1:] for a in v])
            if temp not in perms:
                perms += temp
    return sorted([sorted(list(p)) for p in set([tuple(sorted(p2)) for p2 in perms])])


#perms = rec(perms[0], perms)
#p1 = perms[:]

def getVal(perms):
    perms = rec(perms[0], perms)[:]
    while True:
        prev = perms[:]
        for perm in perms[:]:
            perms = rec(perm, perms)[:]
        #print len(perms), perms
        if perms == prev or len(prev) == len(perms):
            break

    return perms

perms = getVal([[0.02]])[:]
vals[0.02] = perms
print len(perms), perms
perms = getVal([[0.05]])[:]
vals[0.05] = perms
print len(perms), perms
perms = getVal([[0.1]])[:]
vals[0.1] = perms
print len(perms), perms
perms = getVal([[0.5]])[:]
vals[0.5] = perms
print len(perms), perms
perms = getVal([[1.0]])[:]
print len(perms), perms



'''
for perm in perms[:]:
    rec(perm)
for perm in perms[:]:
    rec(perm)
for perm in perms[:]:
    rec(perm)
for perm in perms[:]:
    rec(perm)
for perm in perms[:]:
    rec(perm)
for perm in perms[:]:
    rec(perm)
for perm in perms[:]:
    rec(perm)
for perm in perms[:]:
    rec(perm)
for perm in perms[:]:
    rec(perm)
for perm in perms[:]:
    rec(perm)

'''
#perms = [sorted(perm) for perm in perms]
#print len(perms), perms
#print [0.01, 0.01, 0.01, 0.02, 0.05, 0.2, 0.2, 0.5, 1.0] in perms





