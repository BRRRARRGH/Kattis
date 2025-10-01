input()
houses = input().split()
for i in range(len(houses)):
    houses[i] = int(houses[i])
houses.sort()
numPeople = input().split()
for person in numPeople:
    numAnger = 0
    for i in range(int(person)):
        numAnger += houses[i]
    print(numAnger)