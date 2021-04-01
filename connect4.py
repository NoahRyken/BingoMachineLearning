board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        ]
color = 1

def moveAdder(nextMove):
    global color
    global board
    if board[5][nextMove] != None:
        pass
    for index in range(6):
        if board[5-index][nextMove] == None:
            board[5-index][nextMove] = color
            color *= -1
            break
    return board

def reset():
    global board
    board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        ]

def printBoard():
    global board
    for row in board:
        print(row)

def lastMoveWin(column):
    global board
    global color
    inRow = 0
    level = 0
    winner = color*-1

    for index in range(6):
        if board[index][column] != None:
            level = index
            break
    
    for index in range(6):
        if board[index][column] == winner:
            inRow += 1
        if board[index][column] != winner:
            inRow = 0
        if inRow == 4:
            return True

    inRow = 0
    for piece in board[level]:
        if piece == winner:
            inRow += 1
        if piece != winner:
            inRow = 0
        if inRow == 4:
            return True

    inRow1 = 0
    inRow2 = 0
    locations = [level, column]
    left1 = True
    right1 = True
    left2 = True
    right2 = True

    for index in range(7):
        try:
            if left1 and board[locations[0] + index][locations[1] - index] == winner:
                inRow1 += 1
            else:
                left1 = False
            if right1 and board[locations[0] - index][locations[1] + index] == winner:
                inRow1 += 1
            else:
                right1 = False
        except:
            continue
        try:
            if left2 and board[locations[0] + index][locations[1] + index] == winner:
                inRow2 += 1
            else:
                left2 = False
            if right2 and board[locations[0] - index][locations[1] - index] == winner:
                inRow2 += 1
            else:
                right2 = False
        except:
            continue

    if inRow1 > 4 or inRow2 > 4:
        return True

    return False
    



    
    