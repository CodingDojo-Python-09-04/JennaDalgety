
from flask import Flask, render_template, session, redirect, request

import random

app = Flask(__name__)

app.secret_key = "098hf7b5836b83724bfn3"


@app.route("/")

def index():

    return render_template("index.html")


@app.route("/guess", methods=["POST"])

def guess():

    print("in Guess function")

    past_guesses = []

    session["answer"] = random.randint(1, 10)

    session["guess"] = int(request.form["guess"])

    if session["guess"] == session["answer"]:
        return render_template("you_win.html")
    elif session["guess"] in past_guesses:
        pass
    else:
        past_guesses.append(session["guess"])
        if session["guess"] < session["answer"]:
            return render_template("too_low.html")
        elif session["guess"] > session["answer"]:
            return render_template("too_high.html")



app.run(debug=True)