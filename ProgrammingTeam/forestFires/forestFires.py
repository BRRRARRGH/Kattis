import sys

def genRand(num):
    global r
    r = ((num * 5171) + 13297) % 50021
    return r

def checkToFire(treeA, treeB, treeTemp):
    treeTemp[treeA] = 2
    if(treeA == treeB):
        return 1
    try:
        if(treeTemp[treeA + 100] == 1):
            if checkToFire(treeA + 100, treeB, treeTemp) == 1:
                return 1
    except IndexError:
        pass
    try:
        if(treeTemp[treeA - 100] == 1):
            if checkToFire(treeA - 100, treeB, treeTemp) == 1:
                return 1
    except IndexError:
        pass
    try:
        if(treeTemp[treeA + 1] == 1 and treeA % 100 != 99):
            if checkToFire(treeA + 1, treeB, treeTemp) == 1:
                return 1
    except IndexError:
        pass
    try:
        if(treeTemp[treeA - 1] == 1 and treeA % 100 != 0):
            if checkToFire(treeA - 1, treeB, treeTemp) == 1:
                return 1
    except IndexError:
        pass
    return 0

sys.setrecursionlimit(1000000)

inp:list[str] = sys.stdin.read().strip().split()

it = iter(inp)

n = lambda: int(next(it))

numCases = len(inp) // 2

for _ in range(numCases):
    r = n()
    numQueries = n()
    trees = [0]*10000
    numFires = 0
    fireList = []


    for i in range(numQueries):
        while True:
            genRand(r)
            if trees[r % 10000] == 0:
                trees[r % 10000] = 1
                treeI = r % 10000
                break
        A = genRand(r) % (i+1)
        B = genRand(r) % (i+1)
        newTrees = trees.copy()
        numFires += checkToFire(A, B, newTrees)
        if (i) % 100 == 99:
            fireList.append(numFires)
            numFires = 0
    
    print(fireList)