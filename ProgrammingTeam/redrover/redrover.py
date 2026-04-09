inputString = input()
lowestNumCharacters = len(inputString)

#Loops through 2 --> (len(inputString) / 2) + 1
#ex 01234 --> goes to 2
#ex 012
#ex 012345 --> goes to position 3
#Creates Dictionary with substring as key and number of appearances as value
#Gets max value in dictionary, and calculates lowest num character from that
#Worst case is summation of 99 --> ~3750

for i in range(2, (len(inputString) // 2) + 2):
    substringDictionary = {}
    for j in range(0, len(inputString) - i + 1): 
        if j > 0:
            if inputString[j:j+i] != inputString[j-1:j+i-1]:
                substringDictionary[inputString[j:j+i]] = substringDictionary.get(inputString[j:j+i], 0) + 1
        else:
            substringDictionary[inputString[j:j+i]] = substringDictionary.get(inputString[j:j+i], 0) + 1
    max = 0
    for value in substringDictionary.values():
        if value > max:
            max = value
    smallestIteration = len(inputString) + max + i - (i * max)
    if smallestIteration < lowestNumCharacters:
        lowestNumCharacters = smallestIteration
print(lowestNumCharacters)
