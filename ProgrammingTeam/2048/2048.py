import sys

inp:list = sys.stdin.read().split()

def mergeLeft():
    global board
    global boardCheck


it = iter(inp)

n = lambda: int(next(it))

board = []
boardCheck = []

for x in range(4):
    board.append([n(), n(), n(), n()])
    boardCheck.append([0,0,0,0])

move = n()

match move:
    case 0:
        for x in range(4):
            for y in range(1, 4):
                temp = y
                while(temp > 0):
                    if(board[x][temp-1] == 0):
                        board[x][temp-1] = board[x][temp]
                        board[x][temp] = 0
                    elif(board[x][temp-1] == board[x][temp] and boardCheck[x][temp-1] == 0 and boardCheck[x][temp] == 0):
                        board[x][temp-1] = board[x][temp-1]*2
                        board[x][temp] = 0
                        boardCheck[x][temp-1] = 1
                    else:
                        break
                    temp -= 1
    case 1:
        for y in range(4):
            for x in range(1, 4):
                temp = x
                while(temp > 0):
                    if(board[temp-1][y] == 0):
                        board[temp-1][y] = board[temp][y]
                        board[temp][y] = 0
                    elif(board[temp-1][y] == board[temp][y] and boardCheck[temp-1][y] == 0 and boardCheck[temp][y] == 0):
                        board[temp-1][y] = board[temp-1][y]*2
                        board[temp][y] = 0
                        boardCheck[temp-1][y] = 1
                    else:
                        break
                    temp -= 1
    case 2:
        for x in range(4):
            board[x].reverse()
            for y in range(1, 4):
                temp = y
                while(temp > 0):
                    if(board[x][temp-1] == 0):
                        board[x][temp-1] = board[x][temp]
                        board[x][temp] = 0
                    elif(board[x][temp-1] == board[x][temp] and boardCheck[x][temp-1] == 0 and boardCheck[x][temp] == 0):
                        board[x][temp-1] = board[x][temp-1]*2
                        board[x][temp] = 0
                        boardCheck[x][temp-1] = 1
                    else:
                        break
                    temp -= 1
            board[x].reverse()
    case 3:
        board.reverse()
        for y in range(4):
            for x in range(1, 4):
                temp = x
                while(temp > 0):
                    if(board[temp-1][y] == 0):
                        board[temp-1][y] = board[temp][y]
                        board[temp][y] = 0
                    elif(board[temp-1][y] == board[temp][y] and boardCheck[temp-1][y] == 0 and boardCheck[temp][y] == 0):
                        board[temp-1][y] = board[temp-1][y]*2
                        board[temp][y] = 0
                        boardCheck[temp-1][y] = 1
                    else:
                        break
                    temp -= 1
        board.reverse()
        

print(f"""{board[0][0]} {board[0][1]} {board[0][2]} {board[0][3]}
{board[1][0]} {board[1][1]} {board[1][2]} {board[1][3]}
{board[2][0]} {board[2][1]} {board[2][2]} {board[2][3]}
{board[3][0]} {board[3][1]} {board[3][2]} {board[3][3]}""")