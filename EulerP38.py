
def isPandigital(x):
    if set(str(x)) == set("123456789") and len(str(x)) == 9:
        return True
    return False

initial = 1
MAX = 0


print isPandigital(98191963829457)
while True:
    t = ""
    n = 1
    while len(t) < 9:
        t += str(initial * n)
        if int(t[0]) < int(str(MAX)[0]):
            #print "wait wot"
            break
        n += 1
        if int(t) > MAX:
            MAX = int(t)

    if isPandigital(t):
        print t, initial, n

    if initial > 10**9:
        break


    initial += 1



