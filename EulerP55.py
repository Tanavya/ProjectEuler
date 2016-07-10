
#Lychrel numbers

import time

def isPalindrome(n):
    if str(n)[::-1] == str(n):
        return True
    return False

def isLychrel(x):


    for i in range(50):
        x = x + int(str(x)[::-1])
        if isPalindrome(x):
            return False
    return True


def solve():

    count = 0
    for n in range(11,10001):
        if isLychrel(n):
            count += 1

    return count

start = time.time()
ans = solve()
print "Ans:", ans, "found in", time.time()-start, "seconds"
