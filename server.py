from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import connect4

app = Flask(__name__)
moves = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        global moves
        try:
            if request.form['restart'] == 'Restart':
                moves = []
        except:
            if int(request.form['column']) in range(8):
                moves.append(int(request.form['column']))
    board = connect4.render(moves)
    winner = 0
    #if connect4.lastMoveWin(board):
    #    winner = len(moves) % 2
    return render_template("index.html", display=board, winner=winner)

if __name__ == "__main__":
    app.run(debug=True)