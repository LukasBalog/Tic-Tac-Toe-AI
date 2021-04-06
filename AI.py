import tkinter, math

krizik = input("Zadajte meno hraca pre krizik: ")
koliecko = input("Zadajte meno hraca pre koliecko: ")

canvas = tkinter.Canvas(width=600, height=600, bg="white")
canvas.pack()

canvas.create_line(200, 0, 200, 600)
canvas.create_line(400, 0, 400, 600)
canvas.create_line(0, 200, 600, 200)
canvas.create_line(0, 400, 600, 400)

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
Turn = 0
def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True
def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False
def markWon(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False
def minimax(board, isMaximazing):
    if markWon('X'):
        return 100
    elif markWon('O'):
        return -100
    elif checkDraw():
        return 0
    if isMaximazing:
        bestScore = -1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'X'
                score = minimax(board, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = 800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'O'
                score = minimax(board, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore


def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False

def circle(x, y):
    x = x // 200
    y = y // 200
    canvas.create_oval(0 + (x * 200), 0 + (y * 200), 200 + (x * 200), 200 + (y * 200))


def cross(position):
    if position == 1:
        x = 0
        y = 0
    elif position == 2:
        x = 1
        y = 0
    elif position == 3:
        x = 2
        y = 0
    elif position == 4:
        x = 0
        y = 1
    elif position == 5:
        x = 1
        y = 1
    elif position == 6:
        x = 2
        y = 1
    elif position == 7:
        x = 0
        y = 2
    elif position == 8:
        x = 1
        y = 2
    elif position == 9:
        x = 2
        y = 2
    canvas.create_line(0 + (x * 200), 0 + (y * 200), 200 + (x * 200), 200 + (y * 200))
    canvas.create_line(200 + (x * 200), 0 + (y * 200), 0 + (x * 200), 200 + (y * 200))


if Turn == 0:
        bestScore = -1000
        bestMove = 0
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'X'
                score = minimax(board, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
                    bestMove = key
        cross(bestMove)
        board[bestMove] = 'X'
        Turn = Turn + 1
def draw(event):
    x = event.x
    y = event.y
    global Turn
    if spaceIsFree((x // 200) + 3 * (y // 200) + 1):
        if event.x < 200 and event.y < 200:
            if Turn != 0:
                circle(x, y)
                Turn = Turn - 1
                board[(x // 200) + 3 * (y // 200) + 1] = 'O'
            else:
                bestScore = -1000
                bestMove = 0
                for key in board.keys():
                    if board[key] == ' ':
                        board[key] = 'X'
                        score = minimax(board, False)
                        board[key] = ' '
                        if score > bestScore:
                            bestScore = score
                            bestMove = key
                cross(bestMove)
                board[bestMove] = 'X'
                Turn = Turn + 1
        elif (event.x > 200 and event.x < 400) and event.y < 200:
            if Turn != 0:
                circle(x, y)
                Turn = Turn - 1
                board[(x // 200) + 3 * (y // 200) + 1] = 'O'
            else:
                bestScore = -1000
                bestMove = 0
                for key in board.keys():
                    if board[key] == ' ':
                        board[key] = 'X'
                        score = minimax(board, False)
                        board[key] = ' '
                        if score > bestScore:
                            bestScore = score
                            bestMove = key
                cross(bestMove)
                board[bestMove] = 'X'
                Turn = Turn + 1
        elif (event.x > 400 and event.x < 600) and event.y < 200:
            if Turn != 0:
                circle(x, y)
                Turn = Turn - 1
                board[(x // 200) + 3 * (y // 200) + 1] = 'O'
            else:
                bestScore = -1000
                bestMove = 0
                for key in board.keys():
                    if board[key] == ' ':
                        board[key] = 'X'
                        score = minimax(board, False)
                        board[key] = ' '
                        if score > bestScore:
                            bestScore = score
                            bestMove = key
                cross(bestMove)
                board[bestMove] = 'X'
                Turn = Turn + 1
        elif event.x < 200 and (event.y > 200 and event.y < 400):
            if Turn != 0:
                circle(x, y)
                Turn = Turn - 1
                board[(x // 200) + 3 * (y // 200) + 1] = 'O'
            else:
                bestScore = -1000
                bestMove = 0
                for key in board.keys():
                    if board[key] == ' ':
                        board[key] = 'X'
                        score = minimax(board, False)
                        board[key] = ' '
                        if score > bestScore:
                            bestScore = score
                            bestMove = key
                cross(bestMove)
                board[bestMove] = 'X'
                Turn = Turn + 1
        elif (event.x > 200 and event.x < 400) and (event.y > 200 and event.y < 400):
            if Turn != 0:
                circle(x, y)
                Turn = Turn - 1
                board[(x // 200) + 3 * (y // 200) + 1] = 'O'
            else:
                bestScore = -1000
                bestMove = 0
                for key in board.keys():
                    if board[key] == ' ':
                        board[key] = 'X'
                        score = minimax(board, False)
                        board[key] = ' '
                        if score > bestScore:
                            bestScore = score
                            bestMove = key
                cross(bestMove)
                board[bestMove] = 'X'
                Turn = Turn + 1
        elif (event.x > 400 and event.x < 600) and (event.y > 200 and event.y < 400):
            if Turn != 0:
                circle(x, y)
                Turn = Turn - 1
                board[(x // 200) + 3 * (y // 200) + 1] = 'O'
            else:
                bestScore = -1000
                bestMove = 0
                for key in board.keys():
                    if board[key] == ' ':
                        board[key] = 'X'
                        score = minimax(board, False)
                        board[key] = ' '
                        if score > bestScore:
                            bestScore = score
                            bestMove = key
                cross(bestMove)
                board[bestMove] = 'X'
                Turn = Turn + 1
        elif event.x < 200 and (event.y > 400 and event.y < 600):
            if Turn != 0:
                circle(x, y)
                Turn = Turn - 1
                board[(x // 200) + 3 * (y // 200) + 1] = 'O'
            else:
                bestScore = -1000
                bestMove = 0
                for key in board.keys():
                    if board[key] == ' ':
                        board[key] = 'X'
                        score = minimax(board, False)
                        board[key] = ' '
                        if score > bestScore:
                            bestScore = score
                            bestMove = key
                cross(bestMove)
                board[bestMove] = 'X'
                Turn = Turn + 1
        elif (event.x > 200 and event.x < 400) and (event.y > 400 and event.y < 600):
            if Turn != 0:
                circle(x, y)
                Turn = Turn - 1
                board[(x // 200) + 3 * (y // 200) + 1] = 'O'
            else:
                bestScore = -1000
                bestMove = 0
                for key in board.keys():
                    if board[key] == ' ':
                        board[key] = 'X'
                        score = minimax(board, False)
                        board[key] = ' '
                        if score > bestScore:
                            bestScore = score
                            bestMove = key
                cross(bestMove)
                board[bestMove] = 'X'
                Turn = Turn + 1
        elif (event.x > 400 and event.x < 600) and (event.y > 400 and event.y < 600):
            if Turn != 0:
                circle(x, y)
                Turn = Turn - 1
                board[(x // 200) + 3 * (y // 200) + 1] = 'O'
            else:
                bestScore = -1000
                bestMove = 0
                for key in board.keys():
                    if board[key] == ' ':
                        board[key] = 'X'
                        score = minimax(board, False)
                        board[key] = ' '
                        if score > bestScore:
                            bestScore = score
                            bestMove = key
                cross(bestMove)
                board[bestMove] = 'X'
                Turn = Turn + 1
        if checkDraw():
            print("draw")
        if checkForWin():
            if Turn == 1:
                print(krizik + " je Vitaz")
                #exit()
            else:
                print(koliecko + " je Vitaz")
                #exit()
canvas.bind('<Button-1>', draw)
canvas.mainloop()
