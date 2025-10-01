myInput = input()
#Sample input = len(54)
#1 x 54, 2 x 27, 3 x 18, 6 x 9
#Best # is 6 x 9 
#Sample Input = len(16)
#1x16, 2x8, 4x4
thisList = []
for i in range(len(myInput), 0,-1):
    if((len(myInput) % i) == 0):
        thisList.append(i)
        #Fills list with 54, 27, 18, 9, 6, 3, 2, 1
        #Fills List with 16,8,4,2,1
numRows = thisList[(len(thisList) // 2)] #numRows = 2
numCols = thisList[(len(thisList) // 2) - 1] #numRows = 1
endString = ""
for i in range(0, numRows):
    for j in range(i, len(myInput), numRows):
        endString += myInput[j]
print(endString)


