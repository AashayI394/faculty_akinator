from db_functions import get_department_and_year, get_semester, get_subjects, get_faculties
#testing get_department and year functions
departments, years = get_department_and_year()
print("Departments available: ", departments)
print("Years: ",years)

#test get_semester function
department = "Computer Engineering"
year = "Second Year"
semesters = get_semester(department,year)
print("Semesters: ", semesters)

#test get_subjects function
department="Computer Engineering"
year="Second Year"
semester =3
print()
subjects = get_subjects(department,year,semesters)
print("Subjects: ",subjects)

subject = "Digital Logic Design"
faculties = get_faculties(department,subject)
print("Faculties: ",faculties)