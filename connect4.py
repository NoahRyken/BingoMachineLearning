def render(setUp):
    board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        ]
    color = 1
    for move in setUp:
        if board[5][move-1] != None:
            pass
        for index in range(6):
            if board[5-index][move-1] == None:
                board[5-index][move-1] = color
                color *= -1
                break
    return board

#def printBoard(board):
#    for row in board:
#        print(row)
#
#def lastMoveWin(setUp):
#    board = render(setUp)
#    printBoard(board)
    