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

@app.route("/hello") #decorator demands a method or function for it to decorate @ means decorator
def say_hello():
    #return "Hello there!"
    html = """
    <html>
        <body>
            <h1>Hello!</h1>
            <p>This is the hello page</p>
        </body>
    </html
    """
    return html
# this for whenever someone requests hello page

@app.route("/goodbye")
def say_bye():
    return "Say goodbye"


@app.route("/search")
def search():
    term = request.args["term"]
    sort = request.args["sort"]
    return f"<h1> Search results for: {term}</h1> <p> sorting by {sort}"



@app.route("/add-comment")
def add_comment_form():
    """Show form for adding a comment."""

    return """
        <h1> add comment here</h1>
      <form method="POST">
        <input name="comment">
        <button>Submit</button>
      </form>
      """

@app.route("/add-comment", methods=["POST"])
def add_comment():
    """Handle adding comment."""

    comment = request.form["comment"]


    return f'<h1>Received "{comment}".</h1>'

