class myPy:
    binaryToOctal = {"000":"0", "001":"1", "010":"2", "011":"3", "100":"4","101":"5", "110":"6", "111":"7"}
    binary = input()
    if (len(binary) % 3 == 2):
        newBinary = "0" + binary
    elif (len(binary) % 3 == 1):
        newBinary = "00" + binary
    else: 
        newBinary = binary
    octal = ""
    for i in range(0,len(newBinary), 3):
        shortNum = newBinary[i] + newBinary[i+1] + newBinary[i+2]
        octal += binaryToOctal.get(shortNum)
    print(octal)


