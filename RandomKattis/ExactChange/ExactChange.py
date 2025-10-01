total = int(input())
bills = [0]*5
totals = [1,5,15,30,150]
for i in range(4,-1,-1):
    while((total / totals[i]) >= 1):
        total -= totals[i]
        bills[i] += 1
    bills[i] = str(bills[i])
myStr = " ".join(bills)
print(myStr)



