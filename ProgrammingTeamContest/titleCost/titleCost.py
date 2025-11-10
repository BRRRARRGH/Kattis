myinput = input().split()
word = myinput[0]
myNumber = float(myinput[1])
if(len(word) < myNumber):
    print(str(len(word)))
else:
    print(str(myNumber))