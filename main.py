# Python Flask apliakcija

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/kontakti")
def kontakt():
    return render_template("kontakti.html")

@app.route("/onama")
def onama():
    return "Ovo je stranica o nama!"

if __name__ == "__main__":
    app.run(use_reloader=True)