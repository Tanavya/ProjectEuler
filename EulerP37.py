
def isPrime(n):

    if n == 2:
        return True

    if n > 1 and n % 2 != 0:
        for curr in range(3, int(n**0.5) + 1, 2):
            if n % curr == 0:
                return False
        return True
    return False




def isTruncatablePrime(n):

    n = str(n)
    n_copy = n
    while n:
        if not isPrime(int(n)):
            return False
        n = n[1:]

    n = n_copy
    while n:
        if not isPrime(int(n)):
            return False
        n = n[:-1]


    return True


SUM = 0
count = 0
n = 10
while count < 11:

    if isTruncatablePrime(n):
        print n
        count += 1
        SUM += n
    n += 1


print "SUM:", SUM