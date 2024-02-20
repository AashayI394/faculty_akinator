from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

from app import app

@app.route("/")
def index():
    return render_template("index.html")

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            #error = 'Invalid Credentials. Please try again.'
            return render_template("error.html")
        else:
            return render_template("addquestion.html")
    return render_template("login.html", error=error)


@app.route("/akinator")
def akinator():
    return redirect("https://en.akinator.com/theme-selection")

@app.route("/facinator")
def facinator():
    return render_template("facinator.html")

@app.route("/reset")
def reset():
    return render_template("index.html")

@app.route("/facinator/submit")
def submit():
    return render_template("submit.html")

@app.route("/addnew")
def addnew():
    return render_template("addquestion.html")
