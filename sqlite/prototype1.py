import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('college_faculty.db')
cursor = conn.cursor()

# Create tables
# cursor.execute('''CREATE TABLE IF NOT EXISTS departments (
#                     id INTEGER PRIMARY KEY,
#                     name TEXT NOT NULL
#                 )''')

# cursor.execute('''CREATE TABLE IF NOT EXISTS year_of_study (
#                     id INTEGER PRIMARY KEY,
#                     "year" TEXT NOT NULL
#                 )''')

# cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
#                     id INTEGER PRIMARY KEY,
#                     name TEXT NOT NULL,
#                     department_id INTEGER,
#                     year_of_study_id INTEGER,
#                     semester INTEGER,
#                     FOREIGN KEY (department_id) REFERENCES departments(id),
#                     FOREIGN KEY (year_of_study_id) REFERENCES year_of_study(id)
#                 )''')

# cursor.execute('''CREATE TABLE IF NOT EXISTS faculties (
#                     id INTEGER PRIMARY KEY,
#                     name TEXT NOT NULL,
#                     email TEXT,
#                     department_id INTEGER,
#                     subject_id INTEGER,
#                     FOREIGN KEY (department_id) REFERENCES departments(id),
#                     FOREIGN KEY (subject_id) REFERENCES subjects(id)
#                 )''')

# cursor.execute("SELECT * FROM faculties")

# items = cursor.fetchall()
# for i in items:
#     print(i)

#inserting subjects in subjects table

# many_subjects = [
#                     ('Electronic Devices and Circuits',3,2,3),
#                     ('Digital System Design',3,2,3),            
#                     ('Signals and Systems',3,2,3),
#                     ('Network Synthesis and Analog Filters',3,2,3),
#                     ('Microcontrollers and Applications',3,2,4),
#                     ('Integrated Circuits and Applications',3,2,4),
#                     ('Micro-Project',3,2,4),
#                    ]

# cursor.executemany("INSERT INTO subjects (name,department_id,year_of_study_id,semester) VALUES (?,?,?,?)",many_subjects)
# print("ENTC Subjects Added Successfully...")
# conn.commit()

# #inserting faculties in faculties table
# many_faculties = [
#                     ('Dr. Mahajan S. P.','spm.extc@coeptech.ac.in',3,35),
#                     ('Ms. Agarwal V. S.','vsa.extc@coeptech.ac.in',3,36),
#                     ('Ms. Metkar S. P.','metkars.extc@coeptech.ac.in',3,37),
#                     ('Ms. Kapse Y. D.','ydk.extc@coeptech.ac.in',3,38),
#                     ('Ms. Kolhare N. R.','nrk.extc@coeptech.ac.in',3,39),
#                     ('Ms. More V. N.','vnm.extc@coeptech.ac.in',3,40),
#                     ('Ms. Niture D. V.','dvn.extc@coeptech.ac.in',3,41),
#                     ]

# cursor.executemany("INSERT INTO faculties (name,email,department_id,subject_id) VALUES (?,?,?,?)",many_faculties)
# print("Faculties added...")
# conn.commit()

# cursor.execute("SELECT * FROM subjects") 
# items = cursor.fetchall()

# for i in items:
#     print(i)

# #Execute a query to fetch subjects along with their department and year of study
# cursor.execute('''SELECT s.id, s.name AS subject_name, d.name AS department_name, y.year AS year_of_study, s.semester
#                   FROM subjects s
#                   JOIN departments d ON s.department_id = d.id
#                   JOIN year_of_study y ON s.year_of_study_id = y.id
#                   WHERE department_name LIKE "ENTC%"''')

# results = cursor.fetchall()
# print("Number of rows fetched:", len(results))
# print()
# # # Print the results
# for row in results:
#     print("Subject ID: ", row[0])
#     print("Subject:", row[1])
#     print("Department:", row[2])
#     print("Year of Study:", row[3])
#     print("Semester: ",row[4] )  
#     print() #newline for better formatting


# #Execute a query to fetch faculties along with their department and subject details
# cursor.execute('''SELECT f.id, f.name AS faculty_name, d.name AS department_name, s.name AS subject_name, f.email
#                   FROM faculties f
#                   JOIN departments d ON f.department_id = d.id
#                   JOIN subjects s ON f.subject_id = s.id
#                   WHERE d.name LIKE "ENTC%"''')

# # Fetch all rows from the result set
# results = cursor.fetchall()
# print("Fetching results from faculties table..")
# print()
# # Print the results
# for row in results:
#     print("Faculty ID:", row[0])
#     print("Faculty Name:", row[1])
#     print("Department Name:", row[2])
#     print("Subject Name:", row[3])
#     print("Email ID:", row[4])
#     print()

# cursor.executemany("INSERT INTO faculties (name,email,department_id,subject_id) VALUES (?,?,?,?)",many_faculties)
# print("Faculties added successfully...")
# cursor.execute("""UPDATE subjects SET department_id=1  
#                     WHERE id=16""")
# conn.commit()
# print("Department updated..")

# Commit changes and close the connection
# conn.commit()
conn.close()

# print("26 subjects Added Successfully.")
