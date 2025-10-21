numLines = int(input())
nums = []
topTotal = 0
bottomTotal = 0
total = 0
for x in range(numLines):
    nums.append(int(input()))
nums.sort()
for i in range(numLines):
    topTotal += ((numLines + 1 - (i + 1)) * nums[i])
    bottomTotal += nums[i]

total = topTotal / bottomTotal
total *= 2
total = numLines + 1 - total
total = total / numLines
print(str(total))