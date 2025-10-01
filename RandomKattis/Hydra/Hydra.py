myInput = input()
while(myInput != "0 0"):
    line = myInput.split()
    numHeads = int(line[0])
    numTails = int(line[1])
    numActions = 0
    #SampleInput = 2 3
    while(numHeads != 0 or numTails != 0):
        if(numHeads >= 2): #Heads = 0 or 1
            numHeads -= 2
            numActions += 1
        elif(numTails % 2 == 1): #Tails are even
            numTails += 1
            numActions += 1
        elif(numTails >= 2 and numHeads == 1): 
            numTails -= 2
            numHeads += 1
            numActions += 1
        elif(numTails == 2 and numHeads == 0):
            numTails += 1
            numActions += 1
        elif(numTails % 2 == 0 and numTails != 0):
            numHeads += 1
            numTails -= 2
            numActions += 1
        else:
            break
    if(numHeads == 0 and numTails == 0):
        print(numActions)
    else:
        print(int(-1))
    myInput = input()
