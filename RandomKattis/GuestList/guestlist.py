import sys
inp:list[str] = sys.stdin.readlines()
mySet = set()
inp.pop(0)
for line in inp:
    myList = line.split()
    if myList[0] == '+':
        mySet.add(myList[1])
    if myList[0] == '-':
        mySet.remove(myList[1])
    if myList[0] == '?':
        if(myList[1] in mySet):
            print("Jebb")
        else:
            print("Neibb")