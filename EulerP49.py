import time
import itertools
"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

def isPrime(n):

    if n == 1:
        return False

    if n == 2 or n == 3:
        return True

    elif n % 2 != 0 and n % 3 != 0:

        for curr in range(3, int(n**0.5) + 1, 2):
            if n % curr == 0:
                return False
        return True

    else:
        return False



primes = [n for n in range(1000, 10000) if isPrime(n)]

def solve():

    for a in primes:
        for b in primes:
            if sorted(str(a)) == sorted(str(b)):
                for c in primes:
                    if sorted(str(b)) == sorted(str(c)) and (b-a == c-b != 0):
                        if (a,b,c) != (1487,4817,8147):
                            return str(a) + str(b) + str(c)

def solve2():
    done = []
    for p in primes:
        if p not in done:
            perms = list(set([int("".join(x)) for x in itertools.permutations(str(p))]))
            perms = set(sorted([p for p in perms if p in primes]))
            done += perms
            if len(perms) > 3:
                for a in perms:
                    for b in perms.difference([a]):
                        for c in perms.difference([a,b]):
                            if b-a == c-b > 0:
                                #if (a,b,c) != (1487,4817,8147):
                                print a,b,c, b-a


start = time.time()
#ans = solve()
#print "Ans:", ans, "found in", time.time() - start, "seconds"
#start = time.time()
ans = solve2()
print "Ans2:", ans, "found in", time.time() - start, "seconds"

import math
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def perms(s):
    if(len(s)==1): return [s]
    result=[]
    for i,v in enumerate(s):
        result += [v+p for p in perms(s[:i]+s[i+1:])]
    return result

def increasing(n):

    suma=-1
    maxCount=len(n)/2
    diff=[]
    while maxCount>0:

        suma+=1
        for i in range(len(n)-suma-1):
            tmp=n[i]-n[i+suma+1]
            #print(tmp, n[i],n[i+suma+1])
            diff.append(abs(tmp))
        count={}

        for i in diff:
            for j in n:
                if i+j in n and i+i+j in n:
                    count[i]=[j,j+i,j+i+i]

        maxCount-=1
    return count


primes=[]
start = time.time()
for i in range(1000,10000):
    if is_prime(i):
        primes.append(i)

tempSol=[]
for i in primes:
    if i not in tempSol: #continue
        #tmp=list(set(perms(str(i))))
        tmp2 = list(set([int("".join(x)) for x in itertools.permutations(str(i))]))
        #tmp2=[int(k) for k in tmp]
        counter=0
        tmp1=[]
        for j in tmp2:
            if j in primes:
                tmp1.extend([j])
                counter+=1
        tempSol += tmp1
        if counter >3:
            l = increasing(sorted(tmp1))
            if len(l)!=0:
                print "**",l


print "Ans3:", time.time() - start, "seconds"
