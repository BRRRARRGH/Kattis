import sys
inp:list[str] = sys.stdin.readlines()
firstLine = inp.pop(0).split()
numBooks = int(firstLine[0])
numSearches = int(firstLine[1])
bookList = []
bookDict = {}
for i in range(numBooks):
    myBook = inp.pop(0).split(",")
    bookList.append((myBook[0], myBook[1].strip()))
sorted_list = sorted(bookList, key=lambda x: (x[1], x[0]))
for x in range(len(sorted_list)):
    myLife = sorted_list[x]
    bookDict[myLife[0]] = x + 1
for i in range(numSearches):
    bookToSearch = inp.pop(0).strip()
    if bookToSearch in bookDict:
        print(str(bookDict[bookToSearch]))
    else:

        print("-1")