def f(c,x):
    a = 1

    while a**2 + (x-c-a)**2 != c**2:
        a += 1
        if a > c or a <= 0 or x-c-a <= 0:
            return None
    return [a, x-c-a]



MAX = 0,0
for x in range(10, 1001, 2):


    c = x/3 + 5
    count = 0

    while c < x-c:
        a = f(c,x)
        if a:
            print x, a + [c]
            count += 1
        c += 1

    if count > MAX[0]:
        MAX = count, x


print MAX
