

def isPattern(x):
    #x = [1,2,3,1,2,3,1,2,3]
    mods = []
    for i in range(2,len(x)/2):
        pattern = getSublists(x, i)
        for n in x:
            if range(x[0],x[-1]+1, n) == x:
                print pattern, "nth term", n
        if checkEqual(pattern):
            print pattern, "Each element is equal"
        elif pattern[::-1] == pattern:
            print pattern, "Reversed = original"
        else:
            for j in range(2,15):
                if j not in mods:
                    mods.append(j)
                    modPattern(x,j)

def checkEqual(lst):
    return lst[1:] == lst[:-1]

def modPattern(lst, x):
    p = []
    for j in lst:
        p.append(j%x)
    for i in range(2,len(p)/2):
        pattern = getSublists(p, i)
        if checkEqual(pattern):
            print "mod", x, pattern, "Each element is equal"
            break
        elif pattern[::-1] == pattern:
            print "mod", x,pattern, "Reversed = original"
            break


def getSublists(L, n):
    sublists = []
    for i in range(0,len(L),n):
        if len(L[i:i+n]) == n:
            sublists.append(L[i:i+n])
    return sublists


print isPattern([1,2,4,7,11,15,21])

