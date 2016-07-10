

i = 1
n = ""
while len(n) < 1000000:

    n += str(i)
    i += 1

champernowne_constant = 1
for p in range(7):
    print 10**p, n[10**p-1]
    champernowne_constant *= int(n[10**p-1])

print champernowne_constant