input()
lots = input().split()
for i in range(len(lots)):
    lots[i] = int(lots[i])
lots.sort(reverse=True)
circleHouses = input().split()
for i in range(len(circleHouses)):
    circleHouses[i] = int(circleHouses[i])
squareHouses = input().split()
for i in range(len(squareHouses)):
    squareHouses[i] = (((int(squareHouses[i]) ** 2) * 2) ** 0.5)
allHouses = (circleHouses + squareHouses)
allHouses.sort(reverse=True)
start = 0
total = 0
for i in range(len(lots)):
    for j in range(start, len(allHouses)):
        if(allHouses[j] < lots[i]):
            allHouses.pop(j)
            start = j
            total += 1
            break
print(total)
