corn = input().split()
nLine = input().split()
sum = 0
for i in range(0, 10, 2):
    sum += int(corn[i]) * int(corn[i+1])
print(((sum // 5) * int(nLine[0])) // int(nLine[1]))
