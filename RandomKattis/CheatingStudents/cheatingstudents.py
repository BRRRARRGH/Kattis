numTime = 0
def checkTimes(has, no):
    global numTime
    if(len(doneLocations) == 0):
        return 0
    else:
        return 1

numStudents = int(input())
potlocations = []
doneLocations = []
for x in range(numStudents):
    student = input().split()
    potlocations.append([int(y) for y in student])
print(checkTimes(potLocations, doneLocations))
print(potlocations)