classNums = {"upper":"1", "middle":"2", "lower":"3"} #Dict that changes upper/middle/lower to 1/2/3

numCases = int(input()) #Gets input for the number of cases
for i in range(numCases): #Loops for the number of cases
    myTuples = [] #Sets myTuples List
    numPeople = int(input()) #Gets the number
    for j in range(numPeople):
        line = input().split()
        person = line[0].split(':')
        myGuy = person[0]
        classes = line[1].split('-')
        betterClasses = [classNums[x] for x in classes]
        while(len(betterClasses) < 10):
            betterClasses.insert(0, "2")
        betterClasses.reverse()
        nums = int("".join(betterClasses))
        myTuples.append((betterClasses, myGuy))
    myTuples.sort()
    for j in myTuples:
        print(j[1])
    print("==============================")
        
    
