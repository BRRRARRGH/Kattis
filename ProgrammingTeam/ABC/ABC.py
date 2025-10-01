nums = input().split()
for i in range(len(nums)):
    nums[i] = int(nums[i])
letters = input()
nums.sort()
newlist = ['0', '0', '0']

for i in range(len(letters)):
    if letters[i] == 'A':
        newlist[i] = nums[0]
        newlist[i] = str(newlist[i])
    if (letters[i] == 'B'):
        newlist[i] = nums[1]
        newlist[i] = str(newlist[i])
    if (letters[i] == 'C'):
        newlist[i] = nums[2]
        newlist[i] = str(newlist[i])
mystringy = ' '.join(newlist)
print(mystringy)