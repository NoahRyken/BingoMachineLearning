from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import connect4
import easyComputer
import random
import time

app = Flask(__name__)

def playerMove(val):
    if val in connect4.possible:
        connect4.moveAdder(val)
    if connect4.lastMoveWin(val):
        return connect4.color*-1
    return 0

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
            winner = playerMove(val)
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
            winner = playerMove(val)
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

if __name__ == "__main__":
    app.run(debug=True)