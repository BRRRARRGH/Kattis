import sys
myList = []
mySet = set()
inp:list[str] = sys.stdin.readlines()
inp.pop(0)
for line in inp:
    if line not in mySet:
        mySet.add(line)
        myList.append(line)
for word in myList:
    print(word)