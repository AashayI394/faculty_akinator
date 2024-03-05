
import sqlite3

def get_faculties(department_id, year_of_study, subject_id):
    # Connect to the SQLite database
    conn = sqlite3.connect('facinator.db')
    c = conn.cursor()

    try:
        if department_id == 0 and year_of_study == 0 and subject_id == 0:
            # Return list of all faculties
            c.execute("SELECT faculty_name FROM Facinator_MasterDB_Sheet1")
        elif department_id != 0 and year_of_study == 0 and subject_id == 0:
            # Return faculties with specified department_id
            c.execute("SELECT faculty_name FROM Facinator_MasterDB_Sheet1 WHERE CAST(department_id AS FLOAT) = ?", (department_id,))
        elif department_id == 0 and year_of_study != 0 and subject_id == 0:
            # Return faculties with specified year_of_study
            c.execute("SELECT faculty_name FROM Facinator_MasterDB_Sheet1 WHERE CAST(year_of_study AS FLOAT) = ?", (year_of_study,))
        elif department_id == 0 and year_of_study == 0 and subject_id != 0:
            # Return faculties with specified subject_id
            c.execute("SELECT faculty_name FROM Facinator_MasterDB_Sheet1 WHERE CAST(subject_id AS FLOAT) = ?", (subject_id,))
        else:
            # Return faculties matching all three parameters
            c.execute("SELECT faculty_name FROM Facinator_MasterDB_Sheet1 WHERE CAST(department_id AS FLOAT) = ? AND CAST(year_of_study AS FLOAT) = ? AND CAST(subject_id AS FLOAT) = ?", (department_id, year_of_study, subject_id))

        # Fetch and return the results
        items = c.fetchall()
        return items
    except sqlite3.Error as e:
        print("SQLite error:", e)
    finally:
        # Close the connection
        conn.close()

# # Test the function with sample parameters
# department_id = 8
# year_of_study = 2
# subject_id = 23

# faculties = get_faculties(department_id, year_of_study, subject_id)
# print("Matching faculties:")
# for faculty in faculties:
#     print(faculty[0])  # Printing the first column only (faculty_name)
