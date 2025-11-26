import sys
inp:list[str] = sys.stdin.readlines()
numCases = int(inp.pop(0))
for x in range(numCases):
    currentSmallest = sys.maxsize
    finishedWord = ""
    myDict = {'a':[], 'b':[], 'c':[], 'd':[], 'e':[], 'f':[], 'g':[], 'h':[], 'i':[], 'j':[], 'k':[], 'l':[], 'm':[], 
              'n':[], 'o':[], 'p':[], 'q':[], 'r':[], 's':[], 't':[], 'u':[], 'v':[], 'w':[], 'x':[], 'y':[], 'z':[], }
    inp.pop(0)
    currentLine = inp.pop(0).strip()
    if(len(currentLine) == 0 or len(currentLine) == 1):
        print("-1")
    else:
        for i in range(len(currentLine)):
            for j in myDict[currentLine[i]]:
                if (abs(j - i)) < currentSmallest:
                    currentSmallest = abs(j - i)
                    finishedWord = currentLine[0:min(i, j)] + currentLine[max(i, j):]
                    
            myDict[currentLine[i]].append(i)
        if(len(finishedWord) == 0):
            print("-1")
        else:
            print(finishedWord)