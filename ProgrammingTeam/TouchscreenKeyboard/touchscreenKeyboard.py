def throughKeyboard(myKeyboard, myPhraseLetter, newPhraseLetter):
    originalCharIndexX = 0
    originalCharIndexY = 0
    newCharIndexX = 0
    newCharIndexY = 0
    for i in range(len(myKeyboard)):
         for j in range(len(myKeyboard[i])):
            if (myPhraseLetter == myKeyboard[i][j]):
                originalCharIndexX = i
                originalCharIndexY = j
            if (newPhraseLetter == myKeyboard[i][j]):
                newCharIndexX = i
                newCharIndexY = j
    
    return (abs(newCharIndexX - originalCharIndexX) + abs(newCharIndexY - originalCharIndexY))



numTestCases = int(input())
myKeyboard = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'], ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'], ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
for i in range(numTestCases):
    myInput = input().split()
    myPhrase = myInput[0]
    numLines = int(myInput[1])
    myList = []
    for j in range(numLines):
        newPhrase = input()
        sum = 0
        for char in range(len(newPhrase)):
            distance = throughKeyboard(myKeyboard, myPhrase[char], newPhrase[char])
            sum += distance
        myList.append((sum, newPhrase))
    myList.sort()
    for tuple in myList:
        print(tuple[1] + " " + str(tuple[0]))


