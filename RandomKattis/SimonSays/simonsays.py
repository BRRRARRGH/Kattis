numLines = int(input())
for x in range(numLines):
    myLine = input().split()
    if(len(myLine) >= 2): 
        if(myLine[0] == "simon" and myLine[1] == "says"):
            myLine.pop(0)
            myLine.pop(0)
            print(" ".join(myLine))
        else:
            print()
    else:
        print()