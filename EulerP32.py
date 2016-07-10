def isPandigital(x):

    if set(x) == set("123456789"):
        return True
    return False


exit()
import time

t = time.time()

SUM = [0,[]]
for x in range(1,9999):
    for a in range(1,999):
        if x % a == 0:
            if isPandigital(str(x/a) + str(a) + str(x)):
                if x not in SUM[1]:
                    SUM[0] += x
                    SUM[1].append(x)
                    print x/a, a, x

print SUM[0], time.time() - t, "seconds"
SUM = [0,[]]

for a in range(9999):
    for b in range(9999):
        s = str(a) + str(b) + str(a*b)
        if len(s) > 9:
            break
        if isPandigital(s):
            x = a*b
            if x not in SUM[1]:
                SUM[0] += x
                SUM[1].append(x)
                print a,b, x


print SUM[0], time.time() - t, "seconds"
