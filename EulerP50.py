
"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
import time

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

start = time.time()
m = 1000000
primes = [n for n in range(1,m) if isPrime(n)]

MIN = 5

for i in range(len(primes)):
    tmp = MIN
    if i + tmp > len(primes): break
    s = 0
    while s < m:
        p = primes[i:i+tmp]
        s = sum(p)
        if isPrime(s) and s < m:
            print "No. of terms:", len(p),  "Sum:", sum(p), "Terms:", p
            MIN = tmp
        tmp += 2

    #since a prime no. + prime no. is always not prime, except if pn is 2.
    #if isPrime(sum(primes[i:i+MIN])):
        #print primes[i:i+MIN], sum(primes[i:i+MIN]), MIN
        #MIN += 1

print "Completed in", time.time()-start, "seconds"