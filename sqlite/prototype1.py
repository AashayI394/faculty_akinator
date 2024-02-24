import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('college_faculty.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''CREATE TABLE IF NOT EXISTS departments (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS year_of_study (
                    id INTEGER PRIMARY KEY,
                    "year" TEXT NOT NULL
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    department_id INTEGER,
                    year_of_study_id INTEGER,
                    semester INTEGER,
                    FOREIGN KEY (department_id) REFERENCES departments(id),
                    FOREIGN KEY (year_of_study_id) REFERENCES year_of_study(id)
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS faculties (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT,
                    department_id INTEGER,
                    subject_id INTEGER,
                    FOREIGN KEY (department_id) REFERENCES departments(id),
                    FOREIGN KEY (subject_id) REFERENCES subjects(id)
                )''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Tables created successfully.")
