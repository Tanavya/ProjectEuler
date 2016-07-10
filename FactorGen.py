
import math


def factorGen(x):
    def is_prime(number):
        while True:
            if number == 2:
                return True
            if number > 1 and number % 2 != 0 and number != 2:
                for current in range(3, int(math.sqrt(number) + 1), 2):
                    if number % current == 0:
                        return False
                return True
            return False
    f = 2
    factors = [0,0]
    while x != 1:

        while not is_prime(f):
            f += 1

        while x % f == 0:
            factors[0] = f
            factors[1] += 1
            x = x/f

        if factors != [0,0]:
            yield tuple(factors)

        factors = [0,0]
        f += 1

def divisorGen(n):
    factors = list(factorGen(n))
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return

#for i in divisorGen(100): print i



def divisorCount(n):
    count = 1
    for i in factorGen(n):
        count *= (i[1] + 1)
    return count
import time

gridSize = [20,20]
cache = {}

def find_paths(gridSize):

    n = 0
    if gridSize == [0,0]:
        #print "found"
        return 1

    if gridSize[0] >= 1:
        #print  "Right", [gridSize[0]-1, gridSize[1]]
        cache.setdefault(tuple([gridSize[0]-1, gridSize[1]]), find_paths([gridSize[0]-1, gridSize[1]]))
        n += cache.get(tuple([gridSize[0]-1, gridSize[1]]), find_paths([gridSize[0]-1, gridSize[1]]))
        #n += find_paths([gridSize[0]-1, gridSize[1]])

    if gridSize[1] >= 1:
        #print "Down", [gridSize[0], gridSize[1]-1]
        cache.setdefault(tuple([gridSize[0], gridSize[1]-1]), find_paths([gridSize[0], gridSize[1]-1]))
        n += cache.get(tuple([gridSize[0], gridSize[1]-1]), find_paths([gridSize[0], gridSize[1]-1]))

    return n
start = time.time()
n = find_paths([3,3])
end = time.time()
print "result", n, "in", end-start, "seconds"

