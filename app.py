from flask import Flask, flash, render_template, request, redirect, url_for, jsonify

import random,sqlite3
from guesslogic import generate_random_number, update_params, find_intersection, create_query, delete_query, singlequery, query_all, dept_temp, yos_temp, gender_temp, semester_temp, doc_temp, office_temp,subject_temp,col_header,dept, yos, gender, doc, office,subject


# game logic start
question_thread = []
conn = sqlite3.connect('facinator.db')
cursor = conn.cursor()
result = query_all()
gametuple=[]
col_res = []


def facinator_game(col, res, val):
    global result
    global gametuple
    if len(result) > 1:
        gametuple.append((col, res, val))
        print(gametuple)
        tempres = singlequery(col, res)
        if val == 'no':
            tempres = list(set(result) - set(tempres))
        result = find_intersection(result, tempres)

# def game_reload():
#     global result, col_header,question_thread,col_res,gametuple
#     col_header = ["department_name","subject_name","gender","doctorate","office","year_of_study","semester"]
#     result = query_all()
#     update_params(result)
#     question_thread = []
#     col_res= []
#     gametuple = []
    


# def update_params():
#     global result
#     global dept_temp, yos_temp, gender_temp, semester_temp, doc_temp, office_temp,subject_temp
#     dept_temp = [t[3] for t in result]
#     yos_temp = [t[7] for t in result]
#     gender_temp = [t[9] for t in result]
#     semester_temp = [t[8] for t in result]
#     office_temp = [t[11] for t in result]
#     doc_temp = [t[10] for t in result]
#     subject_temp = [t[6] for t in result]

# game logic end    

app = Flask(__name__)
app.secret_key = 'Facinator'

from app import app
import sqlite3
con = sqlite3.connect("facinator.db")
c = con.cursor()

 #Execute a query to fetch faculties along with their department and subject details
c.execute('''SELECT * FROM admindb''')
table = c.fetchall()
c.execute('''SELECT DISTINCT department_name FROM admindb''')
department = c.fetchall()
c.execute('''SELECT DISTINCT subject_name FROM admindb''')
subject = c.fetchall()
c.execute('''SELECT DISTINCT year_of_study FROM admindb''')
year = c.fetchall()

con.close()


def create_question(col, res):
  
    match col:
        case "department_name":
            q = "Does the Faculty belong to " + res + " department ?"
        case "subject_name":
            q = "Does this Faculty teach the course " + res +" ?"
        case "gender":
            q = "Is the Faculty "+ res +" ?"
        case "doctorate":
            if res == 'yes':
                q = "Does this Faculty member have a PhD ?"
            if res == 'no':
                q = "The Faculty does not hold a PhD ?"

        case "office":
            q = "Is this faculty's office located in the " + res +" ?"
        case "year_of_study":
            q = "Does this Faculty conduct any class year "+ str(res) + " ?"
        case "semester":
            q = "Does the Faculty teach any course of semester " + str(res) + " ?"
    return q

def final_stmt(val):
    if val == "yes":
        q = "I won !"
    elif val == "no":
        q = "I lost."
    return q


@app.route("/")
def index():
    return render_template("layout.html")

@app.route("/facinator_game")
def game_start():
    # game_reload()
    return redirect("/facinator_game_mode")



@app.route("/facinator_game_mode", methods=['GET', 'POST'])
def game_execute():
    global question_thread
    global col_res
    global result
    global col_header
    global gender_temp
    global doc_temp
    # print(result)

    if len(result) == 1:
        return redirect("/final_question")
        # q = "Your Faculty is\n"+ str(result[0][1])
        # return render_template("game.html", q=q)

    if request.method == 'GET':
        update_params(result)
        
        temp = create_query(0)
        if temp == [-1,-1]:
            return redirect("/final_question")
        col = temp[0]
        res = temp[1]
        col_res.append((col,res))

        q = create_question(col, res)

        question_thread.append([q,None])
        return render_template("game.html", q=q, questions = question_thread)
    if request.method == 'POST':
        val = request.form['game_answer']
        question_thread[-1][1] = val

        update_params(result)
        # function call here

        col = col_res[-1][0]
        res = col_res[-1][1]

        # print("\n\n"+ val)
        # # question_thread[-1][1] = val
        print(col_header)
        if val == 'no':
            if col =='gender':
                col_header.remove(col)
                gender_temp2 = list(set(gender_temp) - set(res))
                gender_temp = gender_temp2
            if col=='doctorate':
                col_header.remove(col)
                doc_temp2 = list(set(doc_temp) - set(res))
                doc_temp = doc_temp2
            delete_query(col,res)
        if val == 'yes':
            if col == 'gender':
                gender_temp = list(res)
            if col == 'doctorate':
                doc_temp = list(res)
            if col == 'semester':
                if 'year_of_study' in col_header:
                    col_header.remove('year_of_study')
            col_header.remove(col)
        
        col = col_res[-1][0]
        res = col_res[-1][1]

        # print(col_res,"\n\n")

        facinator_game(col,res,val)
    return redirect("/facinator_game_mode")

@app.route("/final_question", methods=['GET', 'POST'])
def game_complete():
    global result
    global question_thread

    # print(result)
    if len(result) > 1:
        return redirect("/facinator_game_mode")

    if(result):
        q = "Your Faculty is\n"+ str(result[0][1])
    else:
        return redirect("/gameover")
    return render_template("game_final.html", q=q,questions=question_thread)


@app.route("/gameover", methods=['GET', 'POST'])
def gameover():
    global question_thread
    if request.method == 'POST':
        val = request.form['game_answer']
        q = final_stmt(val)
        if val == "yes":
            return render_template("game_over_success.html", q=q, val=val, questions=question_thread)
        # if val == "no":
        #     return render_template("game_over_failure.html", q=q, val=val)
    val = "no"
    q = final_stmt(val)
    return render_template("game_over_failure.html", q=q, val=val, questions=question_thread)



    # game ends





        
     



@app.route("/register")
def register():
    return render_template("register.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

@app.route("/main")
def main():
    random.shuffle(table)
    return render_template("main.html", items=table, department=department, subject=subject, year=year)

@app.route("/clear")
def clear():
    return redirect("/main")

@app.route("/mail", methods=['GET', 'POST'])
def mail():
    if request.method == 'POST':
        email = request.form['id']
    
        con = sqlite3.connect("facinator.db")
        d = con.cursor()
        d.execute("SELECT * FROM admindb WHERE faculty_email = ?", (email,))
        details = d.fetchall()
        con.close()
        return render_template("mail.html", i=details[0], items=table, department=department, subject=subject, year=year, lectures=details)


@app.route("/mail2", methods=['GET', 'POST'])
def mail2():
    if request.method == 'POST':
        name = request.form['res']
        con = sqlite3.connect("facinator.db")
        d = con.cursor()    
        d.execute("SELECT * FROM admindb WHERE faculty_name = ?", (name,))
        details = d.fetchall()
        con.close()
        return render_template("mail.html", i=details[0], items=table, department=department, subject=subject, year=year, lectures=details)
 

depts = None


@app.route("/dept", methods=['GET', 'POST'])
def dept():
    if request.method == 'POST':

        global depts
        depts = request.form['dept']
        
        con = sqlite3.connect("facinator.db")
        q = con.cursor()

        q.execute("SELECT * FROM admindb WHERE department_name = ?", (depts,))
        dept = q.fetchall()

        # Assuming the subject name is stored in the 7th column (index 6) of each tuple
        subject_tuples = set()  # Using a set to keep track of unique subject names

        # Iterate over each tuple in dept
        for entry in dept:
            # Append the subject name to the set
            subject_name = entry[6]
            subject_tuples.add((subject_name,))  # Adding as a single-element tuple to maintain structure

        # Convert the set of tuples back to a list
        subject_tuples = list(subject_tuples)

        con.close()
        return render_template("main.html", items=dept, department=department, subject=subject_tuples, year=year)
    else:
        return redirect("/main")
    
@app.route("/year", methods=['GET', 'POST'])
def yos():
    if request.method == 'POST':

        y = request.form['year']
        
        con = sqlite3.connect("facinator.db")
        q = con.cursor()
        if depts:
            q.execute("SELECT * FROM admindb WHERE year_of_study = ? AND department_name = ?", (y,depts,))
            y = q.fetchall()
        else:
            q.execute("SELECT * FROM admindb WHERE year_of_study = ?", (y,))
            y = q.fetchall()

        subject_tuples = set()  # Using a set to keep track of unique subject names

        # Iterate over each tuple in dept
        for entry in y:
            # Append the subject name to the set
            subject_name = entry[6]
            subject_tuples.add((subject_name,))  # Adding as a single-element tuple to maintain structure

        # Convert the set of tuples back to a list
        subject_tuples = list(subject_tuples)
        con.close()
        return render_template("main.html", items=y, department=department, subject=subject_tuples, year=year)
    else:
        return redirect("/main")
    

@app.route("/subject", methods=['GET', 'POST'])
def subj():
    if request.method == 'POST':

        sub = request.form['subject']

        con = sqlite3.connect("facinator.db")
        q = con.cursor()

        q.execute("SELECT * FROM admindb where subject_name = ?", (sub,))
        sub = q.fetchall()
        subject_tuples = set()  # Using a set to keep track of unique subject names

        # Iterate over each tuple in dept
        for entry in sub:
            # Append the subject name to the set
            subject_name = entry[6]
            subject_tuples.add((subject_name,))  # Adding as a single-element tuple to maintain structure

        # Convert the set of tuples back to a list
        subject_tuples = list(subject_tuples)

        con.close()
        return render_template("main.html", items=sub, department=department, subject=subject_tuples, year=year)
    else:
        return redirect("/main")
    

@app.route("/mailto", methods=['GET', 'POST'])
def mailto():
    if request.method == 'POST':

        email = request.form['email']
        subject = request.form['mailsubject']
        body = request.form['mailbody']

        # print(email, subject, body)

        # return redirect("/login")
        return redirect(f"mailto:{email}?subject={subject}&body={body}")

    
    else:
        return redirect("/main")
    
@app.route("/search", methods=['GET', 'POST'])
def search():
    searchinput = request.form.get("text")

    con = sqlite3.connect("facinator.db")
    q = con.cursor()

    q.execute("SELECT * FROM admindb WHERE faculty_name LIKE '%{}%' OR department_name LIKE '%{}%'".format(searchinput,searchinput))
    res = q.fetchall()

    con.close()

    if searchinput is None:
        return None

    return jsonify(res)

@app.route("/addnew", methods=['GET', 'POST'])
def addnew():
    if request.method == 'GET':
        flash = None
        return render_template("addnew.html", newsession=1)

    # if request.method == 'POST':

    #     data = request.form
    #     # print(data)
    #     name = data.get('addnewname')
    #     email = data.get('addnewemail')
    #     gender = data.get('addnewgender')
    #     department = data.get('addnewdepartment')
    #     course = data.get('addnewcourse')
    #     courseyear = data.get('addnewcourseyear')
    #     coursesemester = data.get('addnewcoursesemester')
    #     status = data.get('phdstatus')
    #     office = data.get('addnewofficelocation')

    #     print(department)

    #     connection = sqlite3.connect('pending.db')

    #     cur = connection.cursor()

    #     cur.execute("INSERT INTO pending (name, email, gender, department, doctorate, office, course, year_of_study, semester) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
    #                 (name, email, gender, department, status, office, course, courseyear, coursesemester)
    #                 )

    #     connection.commit()
    #     connection.close()
    #     return render_template("addnew.html", newsession=0)

@app.route("/editnew", methods=['POST'])
def editnew():
    if request.method == 'POST':
        name = request.form.get('addnewname')
        email = request.form.get('addnewemail')
        gender = request.form.get('addnewgender')
        department = request.form.get('addnewdepartment')
        course = request.form.get('addnewcourse')
        courseyear = request.form.get('addnewcourseyear')
        coursesemester = request.form.get('addnewcoursesemester')
        status = request.form.get('phdstatus')
        office = request.form.get('addnewofficelocation')
        
        if not gender or not department or not office or not courseyear or not coursesemester:
            error = "Please fill all the fields"
            print(error)
            return render_template("addnew.html", newsession=0, error = error)

        print("Name:", name)
        print("Email:", email)
        print("Gender:", gender)
        print("Department:", department)
        print("Course:", course)
        print("Course Year:", courseyear)
        print("Course Semester:", coursesemester)
        print("Status:", status)
        print("Office:", office)

        connection = sqlite3.connect('pending.db')
        cur = connection.cursor()

        cur.execute("INSERT INTO pending (name, email, gender, department, doctorate, office, course, year_of_study, semester) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (name, email, gender, department, status, office, course, courseyear, coursesemester)
                    )

        connection.commit()
        connection.close()
        return render_template("addnew.html", newsession=0)


def convert_semester(semester):
    if semester == 1:
        return "Sem I"
    elif semester == 2:
        return "Sem II"
    elif semester == 3:
        return "Sem III"
    elif semester == 4:
        return "Sem IV"
    elif semester == 5:
        return "Sem V"
    elif semester == 6:
        return "Sem VI"
    elif semester == 7:
        return "Sem VII"
    elif semester == 8:
        return "Sem VIII"

@app.route("/pending", methods=['GET', 'POST'])
def pending():
    if request.method == 'GET':
        con = sqlite3.connect("pending.db")

        cur = con.cursor()
        cur.execute("SELECT * FROM PENDING")

        new_data = cur.fetchall(); 
        con.close()
        return render_template("pending.html",data = list(reversed(new_data)), newsession=1)


    if request.method == 'POST':  
        action =  request.form.get('action')
        id = request.form.get('entry')

        if action == 'EDIT':

            con = sqlite3.connect("pending.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM pending WHERE id = ?", (id,))
            new_data = cur.fetchall(); 
            # cur.execute("DELETE FROM pending WHERE id = ?", (id,))
            # con.commit()
            con.close() 

            print(new_data)
            name = new_data[0][1]
            email = new_data[0][2]
            gender = new_data[0][3]
            department = new_data[0][4]
            phdstatus =new_data[0][5]
            office = new_data[0][6]
            course = new_data[0][7]
            yos = new_data[0][8]
            semester = new_data[0][9]
            if yos == 1:
                yos = "First Year"
            elif yos == 2:
                yos = "Second Year"
            elif yos == 3:
                yos = "Third Year"
            elif yos == 4:
                yos = "Fourth Year"
            semester = convert_semester(int(semester))
            print(yos)
            print(semester)

            return render_template("editdata.html", Dname=name, Demail=email, Dgender=gender, Ddepartment=department, Dphdstatus=phdstatus, Doffice=office, Dcourse=course, Dyos=yos, Dsemester=semester)

        if action == 'SAVE':
        
            ## fetching data from pending
            con = sqlite3.connect("pending.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM pending WHERE id = ?", (id,))
            fetched_data = cur.fetchall(); 
            print(fetched_data)
            new_data = fetched_data[0]


            ## inserting data into main database
            con = sqlite3.connect("facinator.db")
            cur = con.cursor()
            # print(new_data)
            cur.execute("INSERT INTO admindb(faculty_name, faculty_email, department_name, subject_name, year_of_study, semester, gender, doctorate, office) VALUES(?,?,?,?,?,?,?,?,?)",
                        (new_data[1], new_data[2], new_data[4], new_data[7], new_data[8], new_data[9], new_data[3], new_data[5], new_data[6])
                        )
            con.commit()
            con.close()

            # deleting from pending database
            con = sqlite3.connect("pending.db")
            cur = con.cursor()
            cur.execute("DELETE FROM pending WHERE id = ?", (id,))
            con.commit()
            con.close()
            new_data = fetched_data
            return render_template("pending.html",data = list(reversed(new_data)), newsession=0)
        
        if action == 'DELETE':
            con = sqlite3.connect("pending.db")
            cur = con.cursor()
            cur.execute("DELETE FROM pending WHERE id = ?", (id,))
            con.commit()
            cur.execute("SELECT * FROM pending")
            new_data = cur.fetchall(); 
            con.close()
            return render_template("pending.html",data = list(reversed(new_data)), newsession=0)






































# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            #error = 'Invalid Credentials. Please try again.'
            return redirect("/*")
        else:
            return redirect("/admin")
    return render_template("login.html", error=error)
    


### admin function start

@app.route("/admin")
def alldata():
    con = sqlite3.connect("facinator.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM admindb")
    data = cur.fetchall(); 
    con.close()

    return render_template("alldata.html", data =  list(reversed(data)), deleted=0, login=1)


@app.route("/admindelete", methods=['GET', 'POST'])
def admin_delete():
    if request.method == 'POST':
        id = request.form.get('admin_delete')
        print(id)

        con = sqlite3.connect("facinator.db")
        cur = con.cursor()
        cur.execute("DELETE FROM admindb WHERE id = ?", (id,))
        con.commit()

        cur.execute("SELECT * FROM admindb")
        data = cur.fetchall()
        con.close()

    return render_template("alldata.html", data=list(reversed(data)), deleted=1, login=0)

### admin function end
