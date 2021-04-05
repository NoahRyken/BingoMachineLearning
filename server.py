from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import connect4
import easyComputer
import random
import time
import mediumComputer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['gameSelect'] == 'Player Vs. Player':
            return redirect('/playerVsPlayer')
        elif request.form['gameSelect'] == 'Player Vs. Easy':
            return redirect('/playerVsEasy')
        elif request.form['gameSelect'] == 'Easy Vs. Easy':
            return redirect('/easyVsEasy')
        elif request.form['gameSelect'] == 'Medium Vs. Medium':
            return redirect('/mediumVsMedium')
        elif request.form['gameSelect'] == 'Player Vs. Medium':
            return redirect('/playerVsMedium')
    else:
        return render_template("index.html")

@app.route('/playerVsPlayer', methods=['GET', 'POST'])
def playerVsPlayer():
    winner = 0
    if request.method == 'POST':

        try:
            if request.form['reset'] == 'Reset':
                connect4.reset()
        except:
            pass

        try:
            if request.form['home'] == 'Home':
                connect4.reset()
                return redirect('/')
        except:
            pass

        if connect4.full():
            return render_template("playerVsPlayer.html", display=connect4.board, winner=2, color=connect4.color)

        try:
            val = int(request.form['column']) - 1
            winner = connect4.playerMove(val)
        except:
            pass

    return render_template("playerVsPlayer.html", display=connect4.board, winner=winner, color=connect4.color)

@app.route('/playerVsEasy', methods=['GET', 'POST'])
def playerVsEasy():
    winner = 0
    connect4.color = -1
    if request.method == 'POST':

        try:
            if request.form['reset'] == 'Reset':
                connect4.reset()
        except:
            pass

        try:
            if request.form['home'] == 'Home':
                connect4.reset()
                return redirect('/')
        except:
            pass

        if connect4.full():
            return render_template("playerVsEasy.html", display=connect4.board, winner=2, color=connect4.color)
        
        try:   
            val = int(request.form['column']) - 1
            if val in connect4.possible:
                winner = connect4.playerMove(val)
                if winner == 0:
                    winner = easyComputer.move()
        except:
            pass

    return render_template("playerVsEasy.html", display=connect4.board, winner=winner, color=connect4.color)

@app.route('/easyVsEasy', methods=['GET', 'POST'])
def easyVsEasy():
    winner = 0
    if request.method == 'POST':
        
        try:
            if request.form['reset'] == 'Reset':
                connect4.reset()
        except:
            pass

        try:
            if request.form['home'] == 'Home':
                connect4.reset()
                return redirect('/')
        except:
            pass

        if connect4.full():
            return render_template("easyVsEasy.html", display=connect4.board, winner=2, color=connect4.color)

        try:
            if request.form['fullGame'] == 'Full Game':
                while winner == 0:
                    winner = easyComputer.move()
        except:
            pass

        try:
            if request.form['next'] == 'Next':
                winner = easyComputer.move()
                return render_template("easyVsEasy.html", display=connect4.board, winner=winner, color=connect4.color)
        except:
            pass

    return render_template("easyVsEasy.html", display=connect4.board, winner=winner, color=connect4.color)

@app.route('/playerVsMedium', methods=['GET', 'POST'])
def playerVsMedium():
    winner = 0
    connect4.color = -1
    if request.method == 'POST':

        try:
            if request.form['reset'] == 'Reset':
                connect4.reset()
        except:
            pass

        try:
            if request.form['home'] == 'Home':
                connect4.reset()
                return redirect('/')
        except:
            pass

        if connect4.full():
            return render_template("playerVsMedium.html", display=connect4.board, winner=2, color=connect4.color)
        
        try:   
            val = int(request.form['column']) - 1
            if val in connect4.possible:
                winner = connect4.playerMove(val)
                if winner == 0:
                    winner = mediumComputer.move()
                    if winner != 0:
                        mediumComputer.won()
                else:
                    mediumComputer.lost()
        except:
            pass

    return render_template("playerVsMedium.html", display=connect4.board, winner=winner, color=connect4.color)

@app.route('/mediumVsMedium', methods=['GET', 'POST'])
def mediumVsMedium():
    winner = 0
    go = 0
    second = connect4.color*-1
    if request.method == 'POST':
        
        try:
            if request.form['reset'] == 'Reset':
                connect4.reset()
        except:
            pass

        try:
            if request.form['home'] == 'Home':
                connect4.reset()
                return redirect('/')
        except:
            pass

        if connect4.full():
            return render_template("mediumVsMedium.html", display=connect4.board, winner=2, color=connect4.color)
        
        try:
            if request.form['fullGame'] == 'Full Game':
                go = 1
        except:
            pass   

        try:
            if request.form['next'] == 'Next':
                winner = mediumComputer.move()
                if winner == second:
                    mediumComputer.won()
                elif winner != 0:
                    mediumComputer.lost()
                return render_template("mediumVsMedium.html", display=connect4.board, winner=winner, color=connect4.color)
        except:
            pass


        while go == 1 and winner == 0:
            winner = mediumComputer.move()
            if connect4.full():
                break
             

        if go == 1 and winner == second:
            mediumComputer.won()
        elif winner != 0:
            mediumComputer.lost()

    return render_template("mediumVsMedium.html", display=connect4.board, winner=winner, color=connect4.color)

def train(iterations):
    averageWeights = [0, 0, 0, 0, 0, 0, 0]
    maxWeights = [0, 0, 0, 0, 0, 0, 0]
    totalWeightAverage = 0

    print('Running...')

    for _ in range(iterations):
        winner = 0
        second = connect4.color*-1

        while winner == 0:
            if connect4.full():
                connect4.reset()
            winner = mediumComputer.move()

        if winner == second:
            mediumComputer.won()
        elif winner != 0:
            mediumComputer.lost()
        
        for index in range(7):
            totalWeightAverage += mediumComputer.probabilityTable[index]
            averageWeights[index] += mediumComputer.probabilityTable[index]
            if mediumComputer.probabilityTable[index] >= maxWeights[index]:
                maxWeights[index] = mediumComputer.probabilityTable[index]

        connect4.reset()

    with open('mediumComputerWeightsHuman.txt', 'w') as savedData:

        savedData.write('On ' + str(iterations) + ' iterations\n')

        totalWeightAverage /= (iterations*7)
        data = 'The average weight was ' + str(totalWeightAverage)
        savedData.write(data + '\n')
        print(data)

        with open('mediumComputerWeightsAverage.txt', 'w') as averageData:
            for index in range(7):
                averageWeights[index] /= iterations
                if index != 6:
                    end = '\n'
                else:
                    end = ''
                averageData.write(str(int(averageWeights[index])) + end)

                data = 'Index ' + str(index) + ' had an average weight of ' + str(averageWeights[index]) + ' with a maximum of ' + str(maxWeights[index]) + ' and a deviation of ' + str(averageWeights[index] - totalWeightAverage)
                savedData.write(data + '\n')
                print(data)
            averageData.close()
        savedData.close()
    
    with open('mediumComputerWeights.txt', 'w') as data:
        for index in range(7):
            val = mediumComputer.probabilityTable[index]
            if index != 6:
                end = '\n'
            else:
                end = ''
            data.write(str(val) + end)
        data.close()
        


if __name__ == "__main__":
    train(10000)
    app.run(debug=True)