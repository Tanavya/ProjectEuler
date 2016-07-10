
import time
def check(x):

    to_try = [x*n for n in range(2,7)]
    #print to_try

    for e in to_try:
        if sorted(str(e)) != sorted(str(x)): return False
    return True

print check(125874)

def solve():

    x = 10
    while True:

        if check(x) == True:

            return x
        x+=1

start = time.time()
ans = solve()
print "Ans:", ans, "found in", time.time()-start, "seconds"




