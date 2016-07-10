

def toBinary(n):

    binary = ""

    while n:
        binary += str(n%2)
        n /= 2

    return binary[::-1]


def isPalindrome(n):

    if str(n) == str(n)[::-1]:
        return True


SUM = 0

for n in range(1,1000000):

    if isPalindrome(n) and isPalindrome(toBinary(n)):
        print n
        SUM += n


print SUM
