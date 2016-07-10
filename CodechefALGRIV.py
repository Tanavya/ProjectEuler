#https://www.codechef.com/problems/ALGRIV


def getDigitsSum(x):
    sum = 0
    while x:
        sum += x % 10
        x /= 10

    return sum


def seq(x, START):

    NEXT = START
    terms = [NEXT]
    for i in xrange(x+1):
        NEXT += getDigitsSum(NEXT)
        terms.append(NEXT)
    return terms


n = int(raw_input())
ANS = []
for i in range(n):

    INPUT = int(raw_input())
    In = seq(1000, INPUT)
    G1 = seq(1000, 1)
    G3 = seq(1000, 3)
    G9 = seq(1000, 9)
    ans = 0
    for x in In:
        if x in G1:
            ans =   "1 " + str(x)
            break
        elif x in G3:
            ans =  "3 " + str(x)
            break
        elif x in G9:
            ans =  "9 " + str(x)
            break

    ANS.append(ans)


for a in ANS:
    print a