
from FactorGen import divisorCount


def TriNumGen(n):
    SUM = 0
    while True:
        n += 1
        SUM += n
        yield SUM

count = divisorCount(1)
TG = TriNumGen(0)
while count <= 500:
    n = TG.next()
    count = divisorCount(n)
    print count

print n, count


