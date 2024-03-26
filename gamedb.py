import sqlite3

conn = sqlite3.connect('facinator.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS admindb (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    faculty_name TEXT NOT NULL,
    faculty_email TEXT NOT NULL,
    department_name TEXT NOT NULL,
    department_id INTEGER,
    subject_id INTEGER,
    subject_name TEXT NOT NULL,
    year_of_study INTEGER NOT NULL,
    semester INTEGER NOT NULL,
    gender TEXT NOT NULL,
    doctorate TEXT NOT NULL,
    office TEXT NOT NULL
)''')

cursor.execute('''INSERT INTO admindb (id, faculty_name, faculty_email,department_name,department_id,subject_id,subject_name,year_of_study,semester,gender,doctorate,office)
SELECT id, faculty_name, faculty_email,department_name,department_id,subject_id,subject_name,year_of_study,semester,gender,doctorate,office
FROM admindb''')


conn.commit()

conn.close()
