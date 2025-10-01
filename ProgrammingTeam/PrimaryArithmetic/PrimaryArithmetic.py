myInput = input()
while (myInput != "0 0"):
    myInput = myInput.split()
    leftSide = myInput[0]
    while (len(leftSide) % 9 != 0):
        leftSide = "0" + leftSide
    rightSide = myInput[1]
    while (len(rightSide) % 9 != 0):
        rightSide = "0" + rightSide
    numCarries = 0
    carryNum = 0
    for i in range(8, -1, -1):
        total = int(rightSide[i]) + int(leftSide[i]) + carryNum
        if(total >= 10):
            carryNum = 1
            numCarries += 1
        else:
            carryNum = 0
    if (numCarries > 1):
        print(str(numCarries) + " carry operations.")
    elif (numCarries == 1):
        print(str(numCarries) + " carry operation.")
    else:
        print("No carry operation.")
    myInput = input()

