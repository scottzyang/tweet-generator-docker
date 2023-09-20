"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template, request
from markov_higher_order import Markovgram
from flask import Flask
import sys


app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.


@app.route("/", methods=["GET", "POST"])
def home():
    """Route that returns a web page containing the generated text."""
    if request.method == "POST":
        order = int(request.form["order"])
        markovgram = Markovgram("1984.txt", order)
        markovgram.generate_markov_chain()
        markovgram.create_sentence()
        sentence = markovgram.random_sentence
    else:
        sentence = ""
    return render_template("index.html", sentence=sentence)


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
