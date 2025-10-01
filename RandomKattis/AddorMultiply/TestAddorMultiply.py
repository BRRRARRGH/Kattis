try:
    firstLine = input().split()
    numOperations = int(firstLine[1])
    expression = input()
    print(eval(expression))
    for i in range (numOperations):
        myInput = input().split()
        newExpression = list(expression)
        if(myInput[0] == 's'):
            if(myInput[1] != myInput[2]):
                index1 = ((int(myInput[1]) * 2) - 2)
                index2 = ((int(myInput[2]) * 2) - 2)
                temp = newExpression[index1]
                newExpression[index1] = newExpression[index2]
                newExpression[index2] = temp
        elif(myInput[0] == 'f'):
            indexChange = ((int(myInput[1]) * 2) - 1)
            if(newExpression[indexChange] == "+"):
                newExpression[indexChange] = "*"
            else:
                newExpression[indexChange] = "+"
        else:
            for j in range (1, len(newExpression), 2):
                if(newExpression[j] == "+"):
                    newExpression[j] = "*"
                else:
                    if(newExpression[j] == "*"):
                        newExpression[j] = "+"
        expression = "".join(newExpression)
        myNum = eval(expression)
        print(myNum % 1000000007)