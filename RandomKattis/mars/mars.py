year = int(input())
currentYear = [2018, 4]
while(currentYear[0] <= year):
    if(currentYear[0] == year):
        print("yes")
        break
    currentYear[1] += 26
    if(currentYear[1] % 12 == 0):
        currentYear[0] += (currentYear[1] // 12) - 1
        currentYear[1] = currentYear[1] - ((currentYear[1] // 12) * 12) + 12
    else:
        currentYear[0] += (currentYear[1] // 12)
        currentYear[1] = currentYear[1] - ((currentYear[1] // 12) * 12)
if(currentYear[0] > year):
    print("no")