import sys
inp:list[str] = sys.stdin.readlines()
values = inp.pop(0).split()
oppisite = int(values[0])
numPeople = int(values[0]) * 2
numBestFriends = int(values[1])
bestFriends = inp.pop(0).split()
mySet = set()
for friend in bestFriends:
    friend = int(friend)
    mySet.add(friend)
    mySet.add(friend + (numPeople / 2))
placesVisited = set()


def circlePass(start, end, depth):
    print("Start: " + str(start) + "   End: " + str(end))
    if(start not in placesVisited):
        placesVisited.add(start)
        if(start == end):
            return depth
        else:
            depth += 1
            if(start in mySet):
                if(start == 0):
                    return min(circlePass(numPeople - 1, end, depth), circlePass(start + 1, end, depth), circlePass(start + oppisite, end, depth))
                elif(start == numPeople - 1):
                    return min(circlePass(0, end, depth), circlePass(start - 1, end, depth), circlePass(numPeople - oppisite, end, depth))
                else:
                    if(start >= oppisite):
                        return min(circlePass(start + 1, end, depth), circlePass(start - 1, end, depth), circlePass(numPeople - oppisite, end, depth))
                    else:
                        return min(circlePass(start + 1, end, depth), circlePass(start - 1, end, depth), circlePass(numPeople + oppisite, end, depth))
            else:
                if(start == 0):
                    return min(circlePass(numPeople - 1, end, depth), circlePass(start + 1, end, depth))
                elif(start == numPeople - 1):
                    return min(circlePass(0, end, depth), circlePass(start - 1, end, depth))
                else:
                    if(start >= oppisite):
                        return min(circlePass(start + 1, end, depth), circlePass(start - 1, end, depth))
                    else:
                        return min(circlePass(start + 1, end, depth), circlePass(start - 1, end, depth))
    else:
        return 100000000000



for case in inp:
    caseName = case.split()
    start = int(caseName[0])
    end = int(caseName[1])
    placesVisited.clear()
    print(circlePass(start, end, 0))
