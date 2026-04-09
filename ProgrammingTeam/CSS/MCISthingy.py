numLines = int(input())
for x in range(numLines):
    scalingFactor = int(input())
    dimensions = scalingFactor * 5
    cLength = 'C'*dimensions
    sLength = 'S'*dimensions
    spaceLength = " "*dimensions
    cSmall = 'C'*scalingFactor
    sSmall = 'S'*scalingFactor
    spaceBetween = " "*scalingFactor*4
    

    print("Case " + str(x + 1) + ":")
    for y in range(scalingFactor):
        print(cLength + spaceLength + sLength + spaceLength + sLength)
    for y in range(scalingFactor):
        print(cSmall + spaceLength + spaceBetween + sSmall + spaceLength + spaceBetween + sSmall)
    for y in range(scalingFactor):
        print(cSmall + spaceLength + spaceBetween + sLength + spaceLength + sLength)
    for y in range(scalingFactor):
        print(cSmall + spaceLength + spaceBetween + spaceBetween + sSmall + spaceLength + spaceBetween + sSmall)
    for y in range(scalingFactor):
        print(cLength + spaceLength + sLength + spaceLength + sLength)
    for y in range(5):
        print()