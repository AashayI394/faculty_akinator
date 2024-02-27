from db_functions import get_department_and_year, get_semester
#testing get_department and year functions
departments, years = get_department_and_year()
print("Departments available: ", departments)
print("Years: ",years)

#test get_semester function
department = "Instrumentation Engineering"
year = "Second Year"
semesters = get_semester(department,year)
print("Semesters: ", semesters)