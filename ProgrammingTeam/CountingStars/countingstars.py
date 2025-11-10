import sys
sys.setrecursionlimit(1_000_000)
starsCount = 0
Case = 1
grid = []
def checkStars(x, y):
    if(x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])):
        if(grid[x][y] == '-'):
            grid[x][y] = '#'
            checkStars(x+1,y)
            checkStars(x-1,y)
            checkStars(x,y+1)
            checkStars(x,y-1)
                
inp:list[str] = sys.stdin.readlines()

while(len(inp) != 0):
    starsCount = 0
    numChars = inp.pop(0).split()
    for i in range(2):
        numChars[i] = int(numChars[i])
    grid = []
    for i in range(numChars[0]):
        grid.append(list(inp.pop(0).strip("\n")))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j] == '-'):
                starsCount += 1
                checkStars(i, j)
    print("Case " + str(Case) + ": " + str(starsCount))
    Case+= 1

