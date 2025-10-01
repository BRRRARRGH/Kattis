numTestCases = int(input())
for i in range(numTestCases):
    numFridays = 0
    weekIndex = 0
    input()
    Days = input().split()
    for j in range(len(Days)):
        for k in range(1, int(Days[j]) + 1):
            if (k == 13 and weekIndex == 5):
                numFridays += 1
            weekIndex += 1
            if (weekIndex >= 7):
                weekIndex = 0
    print(numFridays)