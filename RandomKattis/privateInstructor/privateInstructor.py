import sys
inp:list[str] = sys.stdin.readlines()
inp.pop(0)
mySet = set(())
for myLine in inp:
    myAction = myLine.split()
    if(myAction[0] == 'A'):
        mySet.add(int(myAction[1]))
    if(myAction[0] == 'D'):
        mySet.discard(int(myAction[1]))
    if(myAction[0] == 'F'):
        bottomNum = int(myAction[1])
        topNum = int(myAction[2])
        numTaken = 0
        numsCheck = topNum - bottomNum + 1
        if(numsCheck < len(mySet)):
                for i in range(bottomNum, topNum + 1):
                    if i in mySet:
                        numTaken += 1
        else:
            for item in mySet:
                if(item >= bottomNum and item <= topNum):
                    numTaken += 1
        print(numsCheck - numTaken)