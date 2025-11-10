import sys
inp:list[str] = sys.stdin.readlines()
numLines = inp.pop(0)
biggestLowerRange = 0
smallestUpperRange = 1000000
for line in inp:
    myLine = line.split()
    small = int(myLine[0])
    big = int(myLine[1])
    if(small > biggestLowerRange):
        biggestLowerRange = small
    if(big < smallestUpperRange):
        smallestUpperRange = big
if smallestUpperRange < biggestLowerRange:
    print("bad news")
else:
    difference = str(smallestUpperRange - biggestLowerRange + 1)
    print(difference + " " + str(biggestLowerRange))