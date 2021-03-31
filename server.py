from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import connect4

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    winner = 0
    if request.method == 'POST':
        try:
            if request.form['restart'] == 'Restart':
                connect4.reset()
        except:
            if int(request.form['column']) in range(8):
                val = int(request.form['column']) - 1
                connect4.moveAdder(val)
            if connect4.lastMoveWin(val):
                winner = connect4.color
    return render_template("index.html", display=connect4.board, winner=winner)

if __name__ == "__main__":
    app.run(debug=True)