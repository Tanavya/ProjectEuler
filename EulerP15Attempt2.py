import time

gridSize = [20,20]



def find_paths(gridSize): #bad rec method lool

    n = 0
    if gridSize[0,0]:
        #print "found"
        return 1

    #if gridSize[0] >= 1:
        #print  "Right", [gridSize[0]-1, gridSize[1]]
    n += find_paths([gridSize[0]-1, gridSize[1]])

    #if gridSize[1] >= 1:
        #print "Down", [gridSize[0], gridSize[1]-1]
    n += find_paths([gridSize[0], gridSize[1]-1])

    return n
"""
start = time.time()
n = find_paths([[int(n) for n in (line.split())] for line in gridSize ])
end = time.time()
print "Experiment 1 result", n, "in", end-start, "seconds"
"""


def solve(sqSize): #I MADE THIS ITS CALLED MEMOIZATION ! Jk i didnt invent that but ya
    x = {(0,1): 1, (1,0): 1}
    #sqSize += 1
    for i in range(sqSize+1):
        for j in range(sqSize+1):
            x.setdefault((i,j), x.get((i,j-1),0) + x.get((i-1,j),0))

    return x[(sqSize,sqSize)]

start = time.time()
n = solve(5000)
end = time.time()
print "Experiment 1 result", n, "in", end-start, "seconds"


def route_num(cube_size): #iterative (havn't understood it completely)
    L = [1] * cube_size
    for i in range(cube_size):
        for j in range(i):
            #print "before-",L, "i", i, "j", j
            L[j] = L[j]+L[j-1]
            #print L, "i", i, "j", j
        L[i] = 2 * L[i - 1]
    return L[cube_size - 1]

start = time.time()
n = route_num(5)
elapsed = (time.time() - start)
print "%s found in %s seconds" % (n,elapsed)



def countRoutes(m,n):
    grid = [[0] * 21] * 21

    for i in range(m+1):
        grid[i][0] = 1

    for i in range(n+1):
        grid[0][i] = 1

    print grid

    for i in range(m):
        for j in range(n):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    print grid
    print grid[m][n]

countRoutes(20,20)