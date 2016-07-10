
import math

def isPandigital(s):
    
    return set(s) == set("123456789")


golden_ratio = (1+math.sqrt(5))/2
def checkFirst(n):

    def mypow( x, n ):
        res=1.0
        for i in xrange(n):
            res *= x
            if res>1E20: res*=1E-10
        return res

    fN = mypow(golden_ratio,n)/math.sqrt(5)
    s = '%f' % fN
    return isPandigital(s[:9])



def fib():

    a,b,n = 1,1,1

    while True:
        if isPandigital(str(a)[-9:]):
            print a
            if checkFirst(n):
                break
        a,b = b, a+b
        b=b%1000000000
        n += 1

    print n

fib()

