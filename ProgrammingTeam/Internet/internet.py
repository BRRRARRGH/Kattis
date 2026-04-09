import sys

sys.setrecursionlimit(1000000)



inp:list = sys.stdin.read().split()

matrix = {}

it = iter(inp)

i = lambda: int(next(it))

numHouses = i()

numConnections = i()

for _ in range(numConnections):
    house1 = i()
    house2 = i()

    matrix.setdefault(house1, []).append(house2)
    matrix.setdefault(house2, []).append(house1)

housesVisited = [0]*(numHouses+1)

def visitHouse(house):
    for connect in matrix[house]:
        if housesVisited[connect] == 0:
            housesVisited[connect] = 1
            visitHouse(connect)


if 1 in matrix.keys():
    housesVisited[1] = 1
    visitHouse(1)

printed = False

for x in range(2, numHouses + 1):
    if housesVisited[x] == 0:
        print(x)
        printed = True

if not printed:
    print("Connected")
