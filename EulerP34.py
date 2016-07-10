

i = 0
factMemo = {0:0, 1:1, 2:2, 3:6 }

def fact(n):
    global factMemo
    if n in factMemo:
        return factMemo[n]
    else:
        factMemo[n] = fact(n-1) * n
        return factMemo[n]

from math import factorial

for i in range(1,9999999):
    x = [factorial(int(l)) for l in str(i)]
    if i == sum(x):
        print i, x
