from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/menu/qbio")
def menu_qbio():
    return render_template("menu_qbio.html")

@app.route("/recensioni/gramsci")
def recenioni_gramsci():
    return render_template("index_review.html")

@app.route("/suggerisci/gramsci")
def suggest_gramsci():
    return render_template("index_suggest.html")

@app.route("/allergeni")
def allergeni():
    return render_template("index_allergeni.html")

def handler(event, context):
    return app.wsgi_app(event, lambda status, headers: None)
