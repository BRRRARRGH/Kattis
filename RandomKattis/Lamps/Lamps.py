myInput = input().split()
numHours = int(myInput[0])
priceOfElectricity = int(myInput[1])

priceOfLow = 60
priceOfIncan = 5
numDays = 0
IncanIncrease = 1000
LowIncrease = 8000
totalHours = 0

while(priceOfLow > priceOfIncan):
    numDays += 1
    totalHours += numHours
    priceOfIncan += (60 * numHours * priceOfElectricity) / 100000
    priceOfLow += (11 * numHours * priceOfElectricity) / 100000
    if (totalHours > IncanIncrease):
        priceOfIncan += 5
        IncanIncrease += 1000
        print("Incandecent bulb purchased")
    if (totalHours > LowIncrease):
        priceOfLow += 60
        print("low bulb purchased")
        LowIncrease += 8000
    print("Price Low: " + str(priceOfLow) + "Price Incan :" + str(priceOfIncan) + "Day: " + str(numDays))


print(numDays)
