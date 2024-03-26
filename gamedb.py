import sqlite3

conn = sqlite3.connect('facinator.db')
cursor = conn.cursor()

# q1="Is Your Faculty in {dept} ?".format(dept=dept)


# header = ["dept", "yos", "gender", "doc", "office"]
# i is random number

#col = header[i]

# if col == dept:
#     res = dept[]



# dept = ["Applied Science","Civil Engineering","Computer Engineering","ENTC Engineering","Electrical Engineering","Instrumentation Engineering","Mathematics","Mechanical Engineering","Metallury & Materials","Physics"]
# yos = [1, 2, 3, 4]
# gender = ["female", "male"]
# doc = ["yes", "no"]
# office = ["Department", "Academic Complex", "ENTC Extension"]
cursor.execute("SELECT DISTINCT department_name FROM admindb")
subs = cursor.fetchall()
dept = []
for sub in subs:
    dept.append(sub[0])
print(dept)
print()

cursor.execute("SELECT DISTINCT year_of_study FROM admindb")
subs = cursor.fetchall()
yos = []
for sub in subs:
    yos.append(sub[0])
print(yos)
print()

cursor.execute("SELECT DISTINCT gender FROM admindb")
subs = cursor.fetchall()
gender = []
for sub in subs:
    gender.append(sub[0])
print(gender)
print()

cursor.execute("SELECT DISTINCT office FROM admindb")
subs= cursor.fetchall()
office = []
for sub in subs:
    office.append(sub[0])
print(office)
print()

cursor.execute("SELECT DISTINCT doctorate FROM admindb")
subs = cursor.fetchall()
doc = []
for sub in subs:
    doc.append(sub[0])
print(doc)
print()


cursor.execute("SELECT subject_name FROM admindb")
subs = cursor.fetchall()
subject = []
for sub in subs:
    subject.append(sub[0])
print(subject)
print()

# res = "Computer Engineering"
# cursor.execute("SELECT * FROM admindb WHERE department_name =? OR gender =? OR doctorate=? OR year_of_study=? OR subject_name = ?",(res,res,res,res,res,))

conn.close()

























# cursor.execute('''CREATE TABLE IF NOT EXISTS admindb (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     faculty_name TEXT NOT NULL,
#     faculty_email TEXT NOT NULL,
#     department_name TEXT NOT NULL,
#     department_id INTEGER,
#     subject_id INTEGER,
#     subject_name TEXT NOT NULL,
#     year_of_study INTEGER NOT NULL,
#     semester INTEGER NOT NULL,
#     gender TEXT NOT NULL,
#     doctorate TEXT NOT NULL,
#     office TEXT NOT NULL
# )''')

# cursor.execute('''INSERT INTO admindb (id, faculty_name, faculty_email,department_name,department_id,subject_id,subject_name,year_of_study,semester,gender,doctorate,office)
# SELECT id, faculty_name, faculty_email,department_name,department_id,subject_id,subject_name,year_of_study,semester,gender,doctorate,office
# FROM admindb''')


conn.commit()

conn.close()
