import sys
myInputs = [int(x) for x in sys.stdin]
caseNum = 1
while(len(myInputs) != 0):
    numInputs = myInputs.pop(0)
    theInputs = []
    sums = set()
    for i in range(numInputs):
        num = myInputs.pop(0)
        theInputs.append(num)
    for i in range(0, len(theInputs) - 1):
        for j in range(i + 1, len(theInputs)):
            sums.add(theInputs[i] + theInputs[j])
    numCases = myInputs.pop(0)
    print("Case " + str(caseNum) + ":")
    for i in range(numCases):
        closestSum = 100000000
        sumToGet = myInputs.pop(0)
        for sum in sums:
            if(abs(sumToGet - sum) < abs(sumToGet - closestSum)):
                closestSum = sum
        print("Closest sum to " + str(sumToGet) + " is " + str(closestSum) + ".")
    caseNum += 1



