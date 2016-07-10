
with open("EulerP13Str", "r") as f:
    number = [line.replace("\n", "") for line in f.readlines()]

NUMS = [int(n) for n in number]
SUM = sum(NUMS)
SUM = str(SUM)
print SUM[:10]


""" more efficient way """

NUMS = [int(n[:11]) for n in number]
SUM = sum(NUMS)
SUM = str(SUM)
print SUM[:10]

#Since only 10 digits are req. you can cut each number down to 11 digits each, the sum of which won't affect more than the 11th digit!
