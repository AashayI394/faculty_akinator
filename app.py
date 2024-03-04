from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

from app import app
import sqlite3
con = sqlite3.connect("college_faculty.db")
c = con.cursor()

 #Execute a query to fetch faculties along with their department and subject details
c.execute('''SELECT f.id, f.name AS faculty_name, d.name AS department_name, s.name AS subject_name, f.email
                  FROM faculties f
                  JOIN departments d ON f.department_id = d.id
                  JOIN subjects s ON f.subject_id = s.id
                  ''')

item = c.fetchall()
















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

@app.route("/home")
def home():
    return render_template("home.html")



@app.route("/register")
def register():
    return render_template("register.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

@app.route("/temp")
def temp():
    return render_template("layout2.html", items=item)

