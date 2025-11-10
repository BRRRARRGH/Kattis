numTime = 0
potLocations = []
doneLocations = []
minLength = 20000
shortestIndex = 0
distance = 0

numStudents = int(input())
for x in range(numStudents):
    student = input().split()
    potLocations.append([int(y) for y in student])
doneLocations.append(potLocations.pop(0))
while(len(potLocations) != 0):
    minLength = 20000
    shortestIndex = 0
    for i in range(len(doneLocations)):
        for j in range(len(potLocations)):
            distance = abs(doneLocations[i][0] - potLocations[j][0]) + abs(doneLocations[i][1] - potLocations[j][1])
            if distance < minLength:
                minLength = distance
                shortestIndex = j
    doneLocations.append(potLocations.pop(shortestIndex))
    numTime += minLength * 2
print(numTime)