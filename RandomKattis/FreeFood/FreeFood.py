numLines = int(input())
myHash = set()
for i in range(numLines):
    newLine = input().split()
    for j in range(int(newLine[0]), int(newLine[1]) + 1):
        myHash.add(j)
print(len(myHash))