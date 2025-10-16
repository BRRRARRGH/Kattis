numWays = 0
def checkLength(length) -> None:
    global numWays
    if(length == 0):
        numWays += 1
    if(length >= 3):
        checkLength(length - 3)
    if(length >= 2):
        checkLength(length - 2)
    if(length >= 1):
        checkLength(length - 1)
    

numMeter = int(input())
checkLength(numMeter)
print(numWays)
