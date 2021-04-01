from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import connect4
import random
import time

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
    else:
        return render_template("index.html")

@app.route('/playerVsPlayer', methods=['GET', 'POST'])
def playerVsPlayer():
    winner = 0
    if request.method == 'POST':
        try:
            if request.form['restart'] == 'Restart':
                connect4.reset()
        except:
            pass
        try:
            if request.form['home'] == 'Home':
                connect4.reset()
                connect4.color = -1
                return redirect('/')
        except:
            pass
        try:
            if int(request.form['column']) in range(8):
                val = int(request.form['column']) - 1
                connect4.moveAdder(val)
            if connect4.lastMoveWin(val):
                winner = connect4.color
        except:
            pass
    return render_template("playerVsPlayer.html", display=connect4.board, winner=winner, color=connect4.color)

@app.route('/playerVsEasy', methods=['GET', 'POST'])
def playerVsEasy():
    winner = 0
    if request.method == 'POST':
        try:
            if request.form['home'] == 'Home':
                connect4.reset()
                connect4.color = -1
                return redirect('/')
        except:
            pass
        try:
            if int(request.form['column']) in range(8):
                val = int(request.form['column']) - 1
                connect4.moveAdder(val)
            if connect4.lastMoveWin(val):
                winner = connect4.color
            else:
                computer = random.randrange(0, 7)
                connect4.moveAdder(computer)
                if connect4.lastMoveWin(computer):
                    winner = connect4.color
        except:
            pass
        try:
            if request.form['restart'] == 'Restart':
                connect4.reset()
                connect4.color = -1
        except:
            pass
        return render_template("playerVsEasy.html", display=connect4.board, winner=winner, color=connect4.color)
    else:
        connect4.color = -1
    return render_template("playerVsEasy.html", display=connect4.board, winner=winner, color=connect4.color)

@app.route('/easyVsEasy', methods=['GET', 'POST'])
def easyVsEasy():
    winner = 0
    if request.method == 'POST':
        try:
            if request.form['home'] == 'Home':
                connect4.reset()
                connect4.color = -1
                return redirect('/')
        except:
            pass
        try:
            if request.form['start'] == 'Start':
                while True:
                    computer = random.randrange(0, 7)
                    connect4.moveAdder(computer)
                    if connect4.lastMoveWin(computer):
                        winner = connect4.color
                        break
                    else:
                        computer = random.randrange(0, 7)
                        connect4.moveAdder(computer)
                        if connect4.lastMoveWin(computer):
                            winner = connect4.color
                            break
                    return render_template("easyVsEasy.html", display=connect4.board, winner=winner, color=connect4.color)
        except:
            pass
        try:
            if request.form['restart'] == 'Restart':
                connect4.reset()
                connect4.color = -1
        except:
            pass
    return render_template("easyVsEasy.html", display=connect4.board, winner=winner, color=connect4.color)

if __name__ == "__main__":
    app.run(debug=True)