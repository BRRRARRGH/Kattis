import sys
inp:list[str] = sys.stdin.readlines()
myDict = {}
myList = []
bigNums = 0
numLines = int(inp.pop())
for i in range(numLines):
    myNum = int(inp.pop(0).strip())
    if myNum not in myDict:
        myList.append(myNum)
    myDict[myNum] = myDict.get(myNum, 0) + 1
myList.sort(reverse=True)
for i in range(len(myList)):
    bigNums += myDict.get(myList[i])
    if(bigNums >= myList[i]):
        print(myList[i])
        break
if bigNums < myList[len(myList) - 1]:
    print("0")