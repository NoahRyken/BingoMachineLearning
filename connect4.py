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
    color = 0
    inRow = 0
    for row in board:
        if row[column] != None and color == 0: 
            color = row[column]
        elif row[column] == color:
            inRow += 1
        elif row[column] == -1*color:
            return False
        if inRow == 4:
            return True
    return False



    
    