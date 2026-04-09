import sys
sys.setrecursionlimit(10000)


def H(recursiveNumber):
    if(recursiveNumber in HDictionary):
         return HDictionary[recursiveNumber]
    if(recursiveNumber <= -8):
         newNum = H(recursiveNumber + 5) + H(recursiveNumber + 4) + H(recursiveNumber + 2)
    if(recursiveNumber >= 10):
         newNum = H(recursiveNumber - 8) + H(recursiveNumber - 5) + H(recursiveNumber - 3)
    HDictionary[recursiveNumber] = newNum
    return newNum








HDictionary = {}
for i in range(-7, 10):
    HDictionary[i] = i
inputList = [int(x) for x in sys.stdin.readlines()]
inputList.pop(0)
for number in inputList:
        print("Case 1: H(" + str(number) + ") = " + str(H(number)))

