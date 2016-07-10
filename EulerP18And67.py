import time

triangle = open("p067_triangle.txt", "r").read()

grid = triangle.split("\n")
grid[:] = [[int(n) for n in (line.split())] for line in grid]
print grid
triangle = grid[:]

"""

def generate_paths(depth, x=0, y=0):
    if x == depth:
        yield ((x, y),)
    else:
        for path in generate_paths(depth, x+1, y):
            yield ((x, y),) + path
        for path in generate_paths(depth, x+1, y+1):
            yield ((x, y),) + path
start = time.time()
MAX = 0
for path in generate_paths(14):
    SUM = sum([grid[m[0]][m[1]] for m in path])
    if  SUM > MAX:
        MAX = SUM

print MAX, time.time() - start




maxSum = 0
start = time.time()
def traverseAll(col, row, s):
    row += 1
    if row == len(triangle):
        global maxSum
        if s > maxSum:
            maxSum = s
        return
    for step in [0,1]: traverseAll(col+step, row, s+triangle[row][col+step])

traverseAll(0,0,triangle[0][0])
print maxSum, time.time() - start
"""
start = time.time()
triangle.reverse()
for i in range(len(triangle)):
    for j in range(len(triangle[i])-1):
        triangle[i+1][j] += max(triangle[i][j], triangle[i][j+1])

print triangle[-1][0], time.time() - start


