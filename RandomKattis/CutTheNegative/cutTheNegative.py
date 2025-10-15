numLines = int(input())
myList = []
finalList = []
for line in range(numLines):
    newList = input().split()
    for x in range(len(newList)):
        newList[x] = int(newList[x])
    myList.append(newList)
for x in range(len(myList)):
    for y in range(len(myList[x])):
        if myList[x][y] != -1:
            finalList.append(str(x + 1) + " " + str(y + 1) + " " + str(myList[x][y]))
print(str(len(finalList)))
for myline in finalList:
    print(myline)