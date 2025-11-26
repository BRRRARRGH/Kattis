numLines = int(input())
myList = [int(x) for x in input().split()]
myDict = {}
mySortedList = sorted(myList)
for i in range(len(mySortedList)):
    myDict[mySortedList[i]] = i
for i in range(len(myList)):
    myList[i] = str(myDict.get(myList[i]))
print(" ".join(myList))
