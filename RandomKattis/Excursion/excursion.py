numLines = int(input())
leastTime = 100000000000000000
myList = [int(input()) for x in range(numLines)]
myList.sort()
for i in range(len(myList) - 1):
    totalTime = 0
    for j in range(0, i):
        totalTime += myList[i] - myList[j]
    for j in range(i+1, len(myList) - 1):
        totalTime += myList[len(myList) - 1] - myList[j]
    if(totalTime < leastTime):
        leastTime = totalTime
print(leastTime)