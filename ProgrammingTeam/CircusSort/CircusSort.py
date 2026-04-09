import sys

def sortClockwise(coordSort:list):
    leftIntercept = coordSort.pop(0)
    rightIntercept = coordSort.pop(len(coordSort) - 1)
    aboveX = []
    belowX = []
    for coord in coordSort:
        if coord[1] > 0:
            aboveX.append(coord)
        else:
            belowX.append(coord)
    belowX.reverse()
    finalList = []
    finalList.append(leftIntercept)
    finalList.append(aboveX)
    finalList.append(rightIntercept)
    finalList.append(belowX)
    return finalList

inp:list[str] = sys.stdin.readlines()

numXIntercepts = 0

numPoints = int(inp.pop(0))

coordinates = inp.pop(0).split()

coordinates = [float(x) for x in coordinates]

doneCoordinates = []

for i in range(numPoints):
    doneCoordinates.append((coordinates[i*2], coordinates[(i*2) + 1]))

doneCoordinates.sort()

circle1 = []
circle2 = []
circle3 = []

for coord in doneCoordinates:
    if numXIntercepts < 2:
        circle1.append(coord)    
    elif numXIntercepts < 4:
        circle2.append(coord)
    else:
        circle3.append(coord)
    if(coord[1] == 0):
            numXIntercepts += 1

print(sortClockwise(circle1))
print(sortClockwise(circle2))
print(sortClockwise(circle3))

#I didn't deal with the formatting but otherwise it works, along with some error code due to my function. 