with open("EulerP11Str", "r", 0) as f:
    grid = [x.replace("\n", "") for x in f.readlines()]

GRID = []
for line in grid:
    GRID.append([int(x) for x in line.split(" ")])


MAX = 0

for y in range(20):
    prod = 1
    for x in range(20):
        
        try:
            right = GRID[y][x] * GRID[y][x+1] * GRID[y][x+2] * GRID[y][x+3]
            if right > MAX:
                MAX = right

        except IndexError:
            pass

        try:
            down = GRID [y][x] * GRID[y+1][x] * GRID[y+2][x] * GRID[y+3][x]
            if down > MAX:
                MAX = down
        except:
            pass
        

        try:
            diagonalRight = GRID[y][x] * GRID[y+1][x+1] * GRID[y+2][x+2]  * GRID[y+3][x+3]
            if diagonalRight > MAX:
                MAX = diagonalRight
                
        except:
            pass

        try:
            diagonalLeft =  GRID[y][x] * GRID[y+1][x-1] * GRID[y+2][x-2]  * GRID[y+3][x-3]
            if diagonalLeft > MAX:
                MAX = diagonalLeft
        except:
            pass


print MAX




