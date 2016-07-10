import EulerP24
memo = {0:1, 1:1}
def fibMemo(n):

    global memo
    if n in memo:
        return memo[n]
    else:
        a,b = 1, 1
        #a,b = memo.values()[-2], memo.values()[-1]
        #s, s2 = memo.keys()[-2], memo.keys()[-1]
        for i in range(n-1):
            a,b = b, a+b
            memo.setdefault(n-1, a)
        return a

def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a
#print fib(4780), len(str(fib(4780)))



fibMemo(5000)

print fibMemo(2749)
print str(fibMemo(541))[-9:]
