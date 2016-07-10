'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 into 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
import timeit
#TOTIME1 = """\

def permute():
    ini = 100 * 100
    f = 999 * 999
    for i in range(ini, f):
        XD = str(i)
        if XD[::-1] == XD:
            for x in range(100,999):
                if i / x < 999 and i % x == 0:
                    yield i, x


for i in permute():
    print i

print i


TOTIME2 = """\
#A BIT SLOWER
def isPalindrome(x):
    XD = str(x)
    if XD[::-1] == XD:
        return True
    else:
        return False


for i in range(100*100, 999*999):
        if isPalindrome(i):
            for x in range(100,999):
                if i % x == 0:
                    print i,x

"""

#print timeit.timeit(TOTIME1, number=1)
#print timeit.timeit(TOTIME2,number=1)
