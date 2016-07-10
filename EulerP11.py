

with open("EulerP11Str", "r") as f:
    grid = f.readlines()

grid = [line.replace("\n", "") for line in grid]
#print grid

def getSubLists(L, n):
    sublists = []
    i = 0
    while i <= len(L) - n:
        sublists.append(L[i:i+n])
        i += 1

    return sublists

def getProducts(grid):
    linear_products = []
    for i in grid:
        for l in getSubLists(i,4):
            prod = 1
            for n in l:
                prod *= int(n)
            linear_products.append((prod,l))

    return linear_products
    #print max([x[0] for x in linear_products])

#print getProducts(grid)
gridL = []
for l in grid:
    gridL.append(l.split())


gridV = []
for i in range(20):
    gridV.append([x.split()[i] for x in grid])


a = [([gridL[j][i+j] for j in range(20-i)]) for i in range(20)]

print gridL
exit()


print max([x[0] for x in getProducts(a)])

gridD = []

for x in range(20):
    j = x
    temp = []
    for i in range(20):
        try:
            temp.append(gridL[j][i])
        except IndexError:
            pass
        j += 1
    gridD.append(temp)

print max([x[0] for x in getProducts(gridD)])

print gridD


gridDL = []
for x in range(20):
    j = x
    temp = []
    for i in range(19, -1, -1):
        try:
            temp.append(gridL[j][i])
        except IndexError:
            pass
        j += 1
    gridDL.append(temp)

print "g", gridDL


print getProducts(gridV)
print getProducts(gridL)
print getProducts(gridD)
print getProducts(gridDL)

print max([x[0] for x in getProducts(gridV)])
print max([x[0] for x in getProducts(gridL)])
print max([x[0] for x in getProducts(gridD)])
print max([x[0] for x in getProducts(gridDL)])


#print gridDL
print gridD
#print gridL
#print gridV