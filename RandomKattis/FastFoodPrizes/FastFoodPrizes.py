numCases = int(input())
for i in range(numCases):
    line = input().split()
    numLines = int(line[0])
    numTypes = line[1]
    myDict = {}
    total = 0
    for j in range(numLines):
        prize = input().split() # 3, 1, 2, 3, 100 # len(5)
        mySet = set()
        for k in range (1, len(prize) - 1):
            mySet.add(prize[k])
        myDict[int(prize[len(prize) - 1])] = mySet
        #If 100, 1, 2, 3 Dictionary is (100 : {1,2,3})
    draws = input().split()
    numDraws = []
    for draw in range(len(draws)):
        for j in range(int(draws[draw])):
            numDraws.append(draw + 1)
    for x, y in myDict.items():
        myBool = True
        while(myBool):
            for z in y:
                if int(z) not in numDraws:
                    myBool = False
            if myBool:
                total += x
                for z in y:
                    numDraws.remove(int(z))
    print(total)
        