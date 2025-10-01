from collections import Counter
n = int(input())
heights = Counter([int(x) for x in input().split()])
x = 0
best = n

for h in sorted(heights.keys()):
    x += heights[h]
    best = min(best, h+n-x)
print(best)
