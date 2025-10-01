bigNum = input().split()
for i in range(len(bigNum)):
    bigNum[i] = int(bigNum[i])
myArr = input().split()
for i in range(len(myArr)):
    myArr[i] = int(myArr[i])
usedNum = []
myNext = []
for j in range(len(myArr)):
    acc = 0
    if (myArr[j] not in usedNum):
        for k in range(len(myArr)):
            if (myArr[j] == myArr[k]):
                acc += 1
        myNext.append((myArr[j], acc))    
        usedNum.append(myArr[j])
sortedList = sorted(myNext, key=lambda x: x[1], reverse=True)
finalList = []
for mytuple in sortedList:
    for i in range(mytuple[1]):
        finalList.append(mytuple[0])
Mystring = ' '.join(str(x) for x in finalList)
print(Mystring)