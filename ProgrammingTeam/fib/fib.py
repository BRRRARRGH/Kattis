fibDict = {0 : 0, 1 : 1}

def findFib(fibNum):
    if(fibNum <= 1):
        return fibNum
    else:
        if(fibNum not in fibDict):
            currentValue = findFib(fibNum - 1) + findFib(fibNum - 2)
            fibDict[fibNum] = currentValue
            return currentValue
        else:
            return fibDict[fibNum]
    
for i in range(1, 101):
    print(str(i) + ":" + str(findFib(i)))