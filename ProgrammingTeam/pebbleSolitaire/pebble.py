import sys

sys.setrecursionlimit(100000)

def play(pebArr):
    minPebbles = []
    for i in range(10):
        if(pebArr[i] == 'o' and pebArr[i+1] == 'o' and pebArr[i+2] == '-'):
            copyList = pebArr[:]
            copyList[i] = '-'
            copyList[i+1] = '-'
            copyList[i+2] = 'o'
            minPebbles.append(play(copyList))
    for i in range(11, 1, -1):
        if(pebArr[i] == 'o' and pebArr[i-1] == 'o' and pebArr[i-2] == '-'):
            copyList = pebArr[:]
            copyList[i] = '-'
            copyList[i-1] = '-'
            copyList[i-2] = 'o'
            minPebbles.append(play(copyList))
    numPebbles = 0
    if(len(minPebbles) == 0):
        for i in range(12):
            if (pebArr[i] == 'o'):
                numPebbles += 1
        return numPebbles
    else:
        return(min(minPebbles))
    
    


numLines = int(input())
for i in range(numLines):
    pebbleArray = [c for c in input()]
    print(play(pebbleArray))