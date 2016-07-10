"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""


n = 1001
sq_grid = [[None for a in xrange(n)] for b in xrange(n)]

r,c = ((n-1)/2, (n-1)/2)

moves = ["r", "d", "l", "u"]
mn = 0
i = 1
def setRC(m,r,c):
    if m == "r": c += 1
    if m == "d": r += 1
    if m == "l": c -= 1
    if m == "u": r -= 1

    return r,c

sq_grid[r][c] = i
while i <= n**2:

    i += 1
    m = moves[mn % 4]
    r,c = setRC(m,r,c)

    try:
        sq_grid[r][c] = i
    except IndexError:
        break
    tr, tc = setRC(moves[(mn+1) % 4],r,c)
    if sq_grid[tr][tc] == None:
        mn += 1

diagonals = set([])

x,y = n-1, 0
while x > 0:

    diagonals.add((x,y))
    diagonals.add((x,y)[::-1])
    x -= 1
    y += 1
x,y = 0,0
while x < n:

    diagonals.add((x,y))
    diagonals.add((x,y)[::-1])
    x += 1
    y += 1

SUM = sum([sq_grid[p[0]][p[1]] for p in diagonals])
print SUM

