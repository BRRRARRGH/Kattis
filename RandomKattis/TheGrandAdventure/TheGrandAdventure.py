numLines = int(input())
for x in range(numLines):
    line = input()
    itemBag = []
    finish = True
    for char in line:
        if char == '$' or char == '|' or char == '*':
            itemBag.append(char)
        elif char == 't':
            try:
                myItem = itemBag.pop()
                if myItem != '|':
                    finish = False
                    break

            except IndexError as e:
                finish = False
                break
        elif char == 'j':
            try:
                myItem = itemBag.pop()
                if myItem != '*':
                    finish = False
                    break
            except IndexError as e:
                finish = False
                break
        elif char == 'b':
            try:
                myItem = itemBag.pop()
                if myItem != '$':
                    finish = False
                    break
            except IndexError as e:
                finish = False
                break
    if not finish:
        print("NO")
    elif len(itemBag) != 0:
        print("NO")
    else:
        print("YES")