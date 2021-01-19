from boggle import Boggle
from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask, request,render_template, session

app = Flask(__name__)
app.config["SECRET KEY"] = "BoggleYourMind"

debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route("/")
def game_board():
    """Creates the gameboard"""
    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("highscore", 0)
    numplays = session.get("numplays", 0)

    return render_template("board.html", board=board,
                           highscore=highscore,
                           numplays=numplays) 

