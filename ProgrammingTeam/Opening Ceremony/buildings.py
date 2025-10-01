input()
buildings = [int(x) for x in input().split()]
buildings.sort(reverse=True)
numMoves = 0

while len(buildings) != 0:
    checkToMove = False
    for i in range(0, len(buildings)):

        if(buildings[i] > len(buildings)):
            buildings.pop(i)
            numMoves+=1
            break
        if(buildings[i] <= len(buildings)):
            checkToMove = True
            break
    if(len(buildings) != 0 and checkToMove == True):
        buildings = [x -1 for x in buildings]
        numMoves+=1
        numZeroes = buildings.count(0)
        for i in range(numZeroes):
            buildings.remove(0)
print(numMoves)