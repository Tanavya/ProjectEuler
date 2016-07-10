
def divisorGen(n):
    yield 1
    for i in range(2, n/2 + 1):
        if n % i == 0:
            yield i

def abundant(n):
    if sum([div for div in divisorGen(n)]) > n:
        return True
    else:
        return False

AbundantNums = [n for n in range(1,28124-12) if abundant(n)]

abSum = set([])
for n1 in AbundantNums:
    for n2 in AbundantNums:
        if n1 + n2 > 28123:
            break
        abSum.add(n1 + n2)


nums = set(range(28124))
ans = nums.difference(abSum)

print sum(list(ans))
