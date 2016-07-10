
# *1, *2, *3, *4, *5, *6..
# 1**, 2**, 3**, 4**, 5**, 6**, 7**, 8**, 9**
# 1*1, 2*1, 3*1, 4*1, 5*1, 6*1, 7*1, 8*1, 9*1
# 1*3 2*3, 3*3...

#print list(set(["".join(x) for x in itertools.permutations("**563")]))

import itertools, time


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


def replacable(n,c):

    count = 0
    primes = []
    for i in range(10):
        if count > c:
            return False
        if count < 10-c and i > 10-c:
            return False
        x = n.replace("*", str(i))
        if isPrime(int(x)) and len(str(int(x))) == len(n):
            primes.append(x)
            count += 1
    if count == c:
        return primes
    return False

count = 0
done = []
def solve():
    for i in range(1,1000000):
        if sorted(str(i)) in done: continue
        s = 1
        n = "*"*s + str(i)
        while len(n) < 6:
            n = "*"*s + str(i)
            perms = list(set(["".join(x) for x in itertools.permutations(n)]))

            for perm in perms:
                if perm[0] == "0": continue
                if perm[-1].isdigit() and int(perm[-1])%2 == 0: continue
                foo = replacable(perm, 8)
                if foo != False:
                    print "found", perm, foo
                    return foo[0]
            s += 1
        done.append(sorted(str(i)))

start = time.time()
ans = solve()
print "Ans:", ans, "found in", time.time()-start, "seconds"




