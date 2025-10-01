input()
trees = input().split()
for tree in range(len(trees)):
    trees[tree] = int(trees[tree])
trees.sort(reverse=True)
total = 0
for day, t in zip(range(1, len(trees)+1), trees):
    if day + t > total:
        total = day + t
print(total + 1)
