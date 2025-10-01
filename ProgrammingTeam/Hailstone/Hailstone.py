sum = 0
num = int(input())
def myHailstone(num:int) -> int:
    global sum
    if (num == 1):
        sum += num
    else:
        if (num % 2 == 1):
            sum += num
            return myHailstone(3 * num + 1)
        if (num % 2 == 0):
            sum += num
            return myHailstone(num // 2)

myHailstone(num)
print(sum)

    