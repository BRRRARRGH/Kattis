base = int(input())
myValues = input().split()
number = input()
myList = []
myTotal = 0
power = 0
while(len(number) != 0):
    for i in range(len(myValues)):
        numToTry = number.find(myValues[i])
        if(numToTry == 0):
            myList.append(myValues[i])
            if(len(number) > len(myValues[i])):
                number = number[len(myValues[i]):]
            else:
                number = ""
for i in range(len(myList) - 1, -1, -1):
    currentNum = myValues.index(myList[i])
    myTotal += (currentNum * (base**power))
    power += 1
print(myTotal)