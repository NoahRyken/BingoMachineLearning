import connect4
import random

with open('mediumComputerWeightsAverage.txt', 'r') as weights:
    num = ''
    probabilityTable = []
    for char in weights.read():
        if char.isnumeric():
            num += char
        else:
            try:
                probabilityTable.append(int(num))
                num = ''
            except:
                pass
    probabilityTable.append(int(num))
    weights.close()

if probabilityTable == []:
    probabilityTable = [1, 1, 1, 1, 1, 1, 1]
probablitiyTableSum = 0
numOfIterations = 0

def rangeFinder():
    global probabilityTable
    global probablitiyTableSum
    probablitiyTableSum = 0
    for index in connect4.possible:
        probablitiyTableSum += probabilityTable[index]

def move():

    computer = -1
    global probabilityTable
    global probablitiyTableSum
    rangeFinder()

    while computer not in connect4.possible:
        computer = random.randrange(0, probablitiyTableSum + 1)
        total = 0
        for index in connect4.possible:
            total += probabilityTable[index]
            if computer <= total:
                computer = index
                break

    connect4.moveAdder(computer)
    if connect4.lastMoveWin(computer):
        return connect4.color*-1
    return 0

def lost(output=False):
    global probabilityTable
    global numOfIterations
    numOfIterations += 1

    for val in range(1, len(connect4.orderedMoves), 2):
        index = connect4.orderedMoves[val]

        if probabilityTable[index] <= 0:
            probabilityTable = [value+1 for value in probabilityTable]
        probabilityTable[index] -= 1
    if output:
        print('Iteration ' + str(numOfIterations) + ' has a probability table of ' + str(probabilityTable))

def won(output=False):
    global probabilityTable
    global numOfIterations
    numOfIterations += 1

    for val in range(1, len(connect4.orderedMoves), 2):
        index = connect4.orderedMoves[val]
        probabilityTable[index] += 1
    if output:
        print('Iteration ' + str(numOfIterations) + ' has a probability table of ' + str(probabilityTable))
