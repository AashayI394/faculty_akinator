import sqlite3

#function to establish connection to the SQLite Database
def get_db_connection():
	conn = sqlite3.connect('college_faculty.db')
	return conn


#function to get department and year of study 
def get_department_and_year():
	conn = get_db_connection()
	cursor = conn.cursor()
	cursor.execute("SELECT name FROM departments")
	departments = cursor.fetchall()
	cursor.execute("SELECT year FROM year_of_study")
	years = cursor.fetchall()
	conn.close()
	return departments, years


#function to get semesters
def get_semester(department, year):
    conn = get_db_connection()
    cursor = conn.cursor()

     # Get department ID
    cursor.execute("SELECT id FROM departments WHERE name = ?", (department,))
    dept_id = cursor.fetchone()
    dept_id = dept_id[0]
    print("Department number: ",dept_id)
    # Get year ID
    cursor.execute("SELECT id FROM year_of_study WHERE year = ?", (year,))
    year_id = cursor.fetchone()
    year_id = year_id[0]
    print("Year number: ",year_id)

    cursor.execute("SELECT DISTINCT semester FROM subjects WHERE department_id = ? AND year_of_study_id = ?", (dept_id, year_id))
    semesters = cursor.fetchall()
    conn.close()
    return semesters


#function to get subjects based on department, semester and year of study
def get_subjects(department, year, semesters):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Get department ID
    cursor.execute("SELECT id FROM departments WHERE name = ?", (department,))
    department_id = cursor.fetchone()[0]

    # Get year ID
    cursor.execute("SELECT id FROM year_of_study WHERE year = ?", (year,))
    year_id = cursor.fetchone()[0]

    # Fetch subjects for each semester
    all_subjects = []
    for semester in semesters:
        cursor.execute("SELECT name FROM subjects WHERE department_id = ? AND year_of_study_id = ? AND semester = ?", (department_id, year_id, semester[0]))
        subjects = cursor.fetchall()
        all_subjects.extend(subjects)

    conn.close()
    return all_subjects

#function to get faculties teaching a subject in a department
def get_faculties(department, subject):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Get department ID
    cursor.execute("SELECT id FROM departments WHERE name = ?", (department,))
    department_id_row = cursor.fetchone()
    if department_id_row is None:
        conn.close()
        return []

    department_id = department_id_row[0]
    print("Department ID:", department_id)

    # Get subject ID
    cursor.execute("SELECT id FROM subjects WHERE name = ?", (subject,))
    subject_id_row = cursor.fetchone()
    if subject_id_row is None:
        conn.close()
        return []

    subject_id = subject_id_row[0]
    print("Subject ID:", subject_id)

    # Fetch faculties for the given department and subject
    cursor.execute("SELECT name FROM faculties WHERE department_id = ? AND subject_id = ?", (department_id, subject_id))
    faculties = cursor.fetchone()

    conn.close()
    return faculties

    conn.close()
    return faculties

	
