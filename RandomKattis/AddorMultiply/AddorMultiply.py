firstLine = input().split()
numOperations = int(firstLine[1])
expression = input()
numbers = [int(expression[x]) for x in range(0, len(expression), 2)] #loops through expression
symbols = [expression[x] for x in range(1, len(expression), 2)] #loops through expression
while("*" in symbols):
    myIndex = symbols.index("*") #loops through expression
    sum = numbers[myIndex] * numbers[myIndex+1]
    numbers.pop(myIndex+1)
    numbers.pop(myIndex)
    numbers.insert(myIndex, sum)
    symbols.pop(myIndex)
        
while("+" in symbols):
    myIndex = symbols.index("+") #loops through expression
    sum = numbers[myIndex] + numbers[myIndex+1]
    numbers.pop(myIndex+1)
    numbers.pop(myIndex)
    numbers.insert(myIndex, sum)
    symbols.pop(myIndex)

print(numbers[0] % 1000000007)

for i in range (numOperations): #loops through num expressions
    myInput = input().split()
    newExpression = list(expression) #loops through expression
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
    numbers = [int(expression[x]) for x in range(0, len(expression), 2)]
    symbols = [expression[x] for x in range(1, len(expression), 2)]
    while("*" in symbols):
        myIndex = symbols.index("*")
        sum = numbers[myIndex] * numbers[myIndex+1]
        numbers.pop(myIndex+1)
        numbers.pop(myIndex)
        numbers.insert(myIndex, sum)
        symbols.pop(myIndex)
            
    while("+" in symbols):
        myIndex = symbols.index("+")
        sum = numbers[myIndex] + numbers[myIndex+1]
        numbers.pop(myIndex+1)
        numbers.pop(myIndex)
        numbers.insert(myIndex, sum)
        symbols.pop(myIndex)
    print(numbers[0] % 1000000007)