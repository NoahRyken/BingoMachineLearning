board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        ]
color = 1
fullness = [0] * 7
possible = range(7)

def moveAdder(nextMove):
    global color
    global board
    global fullness
    if fullness[nextMove] < 6:
        for index in range(6):
            if board[5-index][nextMove] == None:
                board[5-index][nextMove] = color
                color *= -1
                fullness[nextMove] += 1
                return True
    else:
        return False

def reset():
    global board
    global fullness
    possible = [range(7)]
    fullness = [0] * 7
    board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        ]

def full():
    global fullness
    global possible
    possible = []
    for index in range(7):
        if fullness[index] != 6:
            possible.append(index)
            
    if len(possible) == 0:
        return True
    return False

def printBoard():
    global board
    for row in board:
        print(row)

def lastMoveWin(column):
    global board
    global color
    inRow = 0
    winner = color*-1
    level = -1

    
    for index in range(6):
        if level == -1 and board[index][column] != None:
            level = index
    if level == -1:
        raise ValueError
        
    for index in range(6):
        if board[index][column] == winner:
            inRow += 1
        else:
            inRow = 0
        if inRow >= 4:
            return True
    
    inRow = 0
    for index in range(7):
        if board[level][index] == winner:
            inRow += 1
        else:
            inRow = 0
        if inRow >= 4:
            return True

    inRow = 1
    goL = True
    goR = True

    for distance in range(1, 7):

        if goR and level + distance <= 5 and column + distance <= 6:
            if board[level + distance][column + distance] == winner:
                inRow += 1
            else:
                goR = False

        if goL and level - distance >= 0 and column - distance >= 0:
            if board[level - distance][column - distance] == winner:
                inRow += 1
            else:
                goL = False

        if inRow >= 4:
            return True

    inRow = 1
    goL = True
    goR = True

    for distance in range(1, 7):

        if goR and level - distance >= 0 and column + distance <= 6:
            if board[level - distance][column + distance] == winner:
                inRow += 1
            else:
                goR = False

        if goL and level + distance <= 5 and column - distance >= 0:
            if board[level + distance][column - distance] == winner:
                inRow += 1
            else:
                goL = False

        if inRow >= 4:
            return True

    return False
    



    
    