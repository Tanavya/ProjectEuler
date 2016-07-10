
import Euler10


def PrimeFactors(x, factors):
    #x = 600851475143

    for i in xrange(3, int(x**0.5)+1, 2):
        if x % i == 0:
            #print i,x
            print i
            x = x/i
            factors.append(i)
            return PrimeFactors(x, factors)

    return factors+[x]


print PrimeFactors(600851475143, [])
