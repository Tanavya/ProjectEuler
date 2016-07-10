
import random


def solve():

    with open("p099_base_exp.txt", "r") as f:
        base_exp = [x.replace("\n", "").split(",") for x in f.readlines()]



    bases = [int(x[0]) for x in base_exp]
    exps = [int(x[1]) for x in base_exp]

    multbe = [(i, bases[i], exps[i],bases[i] + exps[i]) for i in range(len(bases))]




    sorted_be = sorted(multbe, reverse=True, key = lambda e: e[2])

    to_check = [e[:3] for e in sorted_be[300:]]


    to_check[:] = [(e[1], e[2]) for e in to_check]
    for e in to_check:
        print "TOCHECK", e
    print sorted_be

    base_exp = {e[0]:(e[1],e[2]) for e in zip(bases, exps, range(len(bases)))}

    #print base_exp

    print base_exp[992372], "lol"


    # 273 !!!!!!

    x = sorted(bases, reverse=True)[:501]
    y = sorted(exps, reverse=True)[:501]

    for e in x:

        if base_exp[e][0] in y:
            print "HEY", e, base_exp[e]


    print base_exp[992372]
    print base_exp[992756]
    print bases[315]




    print len(bases), "LEN"
    print min(bases), max(bases)
    print min(exps), max(exps)
    print max(exps), bases[exps.index(max(exps))], exps.index(max(exps))

    """
    BasesEnum = dict([list(x)[::-1] for x in list(enumerate(bases))])
    ExposEnum = dict([list(x)[::-1] for x in list(enumerate(exps))])



    a = sorted([int(x) for x in bases], reverse=True)
    b = sorted([int(y) for y in exps], reverse=True)
    """
    m = [0,0]
    for e in to_check:

        print e
        x = pow(e[0], e[1])
        #print x
        if x > m[0]:
            m = [x,(e[0],e[1])]

    print m[1], base_exp[m[1][0]]
#solve()


import string
import math
#f = file("base_exp_99.txt")
with open("p099_base_exp.txt", "r") as f:
        num = f.readlines()

max = 0.0
mi = 0
ma = 0
mb = 0
for i in range(0,len(num)-1):
    [a , b] = (num[i]).split(",")
    [a,b] = int(a), int(b)
    n = b*math.log(a,10)
    if n>max:
        mi = i
        max = n
        ma = a
        mb = b
print (mi+1),' ',max,' ',ma,' ',mb


"""
bases = [random.randint(100,1000) for x in range(10)]
exps = [random.randint(100,1000) for y in range(10)]

for i in range(len(bases)):
    print pow(bases[i], exps[i])
"""
"""

M = []
for t in range(4):

    m = [0,0]

    for i in range(len(bases)):
        a,b = bases[i], exps[i]
        #print a,b,a**b
        if a**b>m[0]**m[1]:
            m = [a,b]

    print m

    M.append(m)

    bases = [e/10 for e in bases]
    exps = [e/10 for e in exps]

print M

"""


#x = pow(992756,501148)
#print x
