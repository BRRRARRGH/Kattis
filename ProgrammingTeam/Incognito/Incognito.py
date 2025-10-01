numInputs = int(input())
for i in range(numInputs):
    Categories = {}
    numAttributes = int(input())
    for j in range(numAttributes):
        myInput = input().split()
        Categories[myInput[1]] = Categories.get(myInput[1], 1) + 1
    acc = 1
    for j in Categories.values():
        acc = acc * j
    print(acc - 1)
