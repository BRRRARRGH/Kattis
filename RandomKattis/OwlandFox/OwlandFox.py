numLines = int(input())
for i in range(numLines):
    num = list(input())
    for j in range(len(num) - 1, -1, -1): 
        if (num[j] != '0'):
            num[j] = str(int(num[j]) - 1)
            break
    newNum = "".join(num)
    print(int(newNum))