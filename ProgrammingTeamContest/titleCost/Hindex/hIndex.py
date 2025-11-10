import sys
inp:list[str] = sys.stdin.readlines()
myDict = {}
numLines = int(inp.pop())
for i in range(numLines):
    myNum = int(inp.pop(0))
    myDict[myNum] = myDict.get(myNum, 0) + 1
for i in myDict:
    print(str(i))