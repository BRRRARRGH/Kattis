def syllableCheck(phrase, syllables):
    if(phrase == "" and syllables == 0):
        return True
    if(phrase != "" and syllables == 0):
        return False
    for s in myList:
        if phrase.startswith(s):
            if(syllableCheck(phrase[len(s):].strip(), syllables - 1)):
                return True
    return False






numLines = int(input())
myList = []
for x in range(numLines):
    myList.append(input())
line1 = syllableCheck(input(), 5)
line2 = syllableCheck(input(), 7)
line3 = syllableCheck(input(), 5)



if(line1 and line2 and line3):
    print("haiku")
else:
    print("come back next year")


