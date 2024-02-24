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

#inserting subjects in subjects table
# many_subjects = [
#                     (1,'Linear Algebra',6,1,1),
#                     (2,'Optics and Modern Physics',5,1,1),
#                     (3,'Applied Chemistry',4,1,1),
#                     (4,'Foundations of Mechanical Engineering',2,1,1),
#                     (5,'Problem Solving using Python',1,1,1),
#                     (6,'Electronics and Computer Workshop',3,1,1),
#                     (7,'Univariate Calculus',6,1,2),
#                     (8,'Basic Electrical Engineering',7,1,2),
#                     (9,'Engineering Mechanics',9,1,2),
#                     (10,'Engineering Graphics and Design',2,1,2),
#                     (11,'Semiconductor Physics and Electromagnetism',5,1,2),
#                     (12,'Digital Logic and Design',1,2,3),
#                     (13,'Data Structures and Algorithms-I',1,2,3),
#                     (14,'Principles of Programming Languages',1,2,3),
#                     (15,'Feedback Control Systems',8,2,3),
#                     (16,'Discrete Structures and Graph Theory',6,2,3),
#                     (17,'Ordinary Differential Equations',6,2,3),
#                     (18,'Development Tools Laboratory',1,2,3),
#                     (19,'PLEVH',4,2,3),
#                     (20,'Vector Calculus',6,2,4),
#                     (21,'Data Communication',1,2,4),
#                     (22,'Microprocessor Techniques',1,2,4),
#                     (23,'Sensors and Automation',8,2,4),
#                     (24,'Data Structures and Algorithms-II',1,2,4),
#                     (25,'Biology For Engineers',4,2,4),
#                     (26,'RPPOOP',1,2,4),
#                 ]

# cursor.executemany("INSERT INTO subjects VALUES (?,?,?,?,?)",many_subjects)


# cursor.execute("SELECT * FROM subjects") 
# items = cursor.fetchall()

# for i in items:
#     print(str(i[0])+" | "+i[1])

# Execute a query to fetch subjects along with their department and year of study
cursor.execute('''SELECT s.id, s.name AS subject_name, d.name AS department_name, y.year AS year_of_study, s.semester
                  FROM subjects s
                  JOIN departments d ON s.department_id = d.id
                  JOIN year_of_study y ON s.year_of_study_id = y.id''')

# # Fetch all rows from the result set
# cursor.execute("SELECT * FROM subject")
results = cursor.fetchall()

print("Number of rows fetched:", len(results))
print()
# Print the results
for row in results:
    print("Subject:", row[1])
    print("Department:", row[2])
    print("Year of Study:", row[3])
    print("Semester: ",row[4] )  
    print() #newline for better formatting



#INSERT DEPARTMENT AND YEAR_OF_STUDY
# many_dept = [
#                 ('Computer Engineering',),
#                 ('Mechanical Engineering',),
#                 ('ENTC Engineering',),
#                 ('Applied Science',),
#                 ('Physics',),
#                 ('Mathematics',),
#                 ('Electrical Engineering',),
#                 ('Instrumentation Engineering',),
#                 ('Civil Engineering',),
#             ]
# many_years = [
#                 ('First Year',),
#                 ('Second Year',),
#                 ('Third Year',),
#                 ('Fourth Year',),
#              ]

# Commit changes and close the connection
# conn.commit()
conn.close()

# print("26 subjects Added Successfully.")
