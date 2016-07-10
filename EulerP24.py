"""
import itertools


#print [ "".join(x) for x in itertools.permutations(s)]

def permute2(s):
    return [s] if len(s) == 1 else [c + perm for i, c in enumerate(s) for perm in permute2(s[:i]+s[i+1:])]


s = "MyWord"
print permute2(s)
print [ "".join(x) for x in itertools.permutations(s)]
"""

import itertools

def permute(str):

    res = []

    if len(str) == 2:
        res = [str[1] + str[0], str]

    else:
        for i, c in enumerate(str):
            res += [c + perm for perm in permute(str[:i] + str[i+1:])]

    return res

import time
start = time.time()

lexic =  sorted([ "".join(x) for x in itertools.permutations("0123456789")])
print lexic[1000000-1], time.time() - start, "seconds"

start = time.time()
lexic = sorted([int(x) for x in permute("0123456789")])
print lexic[1000000-1], time.time() - start, "seconds"
