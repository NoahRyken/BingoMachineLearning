import connect4
import random

def move():
    computer = connect4.possible[random.randrange(0, len(connect4.possible))]
    connect4.moveAdder(computer)
    if connect4.lastMoveWin(computer):
        return connect4.color*-1
    return 0