import sqlite3, random
from math import ceil

# Function to query the database based on user choices
# def query_faculty(criteria):
# 	db_path = 'facinator.db'
# 	with sqlite3.connect(db_path) as conn:
# 		cursor = conn.cursor()
# 		query = "SELECT * from admindb WHERE " + " AND ".join(criteria)
# 		cursor.execute(query)
# 		result = cursor.fetchall()
# 		print(result)
# 		print()
# 	return result


col_header = ["department_name","subject_name","gender","doctorate","office","year_of_study","semester"]

conn = sqlite3.connect('facinator.db')
cursor = conn.cursor()
cursor.execute("SELECT DISTINCT department_name FROM admindb")
subs = cursor.fetchall()
dept = []
for sub in subs:
    dept.append(sub[0])
    dept_temp = dept

cursor.execute("SELECT DISTINCT year_of_study FROM admindb")
subs = cursor.fetchall()
yos = []
for sub in subs:
    yos.append(sub[0])
    yos_temp = yos

semester_temp = [1,2,3,4,5,6,7,8]

cursor.execute("SELECT DISTINCT gender FROM admindb")
subs = cursor.fetchall()
gender = []
for sub in subs:
    gender.append(sub[0])
    gender_temp = gender

cursor.execute("SELECT DISTINCT office FROM admindb")
subs= cursor.fetchall()
office = []
for sub in subs:
    office.append(sub[0])
    office_temp = office

cursor.execute("SELECT DISTINCT doctorate FROM admindb")
subs = cursor.fetchall()
doc = []
for sub in subs:
    doc.append(sub[0])
    doc_temp = doc

cursor.execute("SELECT subject_name FROM admindb")
subs = cursor.fetchall()
subject = []
for sub in subs:
    subject.append(sub[0])
    subject_temp = subject

def query_all():
    conn = sqlite3.connect('facinator.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM admindb")
    result = cursor.fetchall()
    return result
    conn.close()

def singlequery(column, res):
    conn = sqlite3.connect('facinator.db')
    cursor = conn.cursor()
    query= f"SELECT * FROM admindb WHERE {column} = ?"
    cursor.execute(query,(res,))
    result = cursor.fetchall()
    conn.close()
    return result

def generate_random_number(length):
    
    return random.randint(0, length - 1)

def find_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = list(set1 & set2)
    return intersection

# def query_subjects1(years):
#     conn = sqlite3.connect('facinator.db')
#     cursor = conn.cursor()
#     cursor.execute("SELECT DISTINCT subject_name FROM admindb WHERE year_of_study IN ({})".format(",".join(map(str, years))))
#     subjects = cursor.fetchall()
#     return [subject[0] for subject in subjects]

# def query_subjects2(sem):
#     conn = sqlite3.connect('facinator.db')
#     cursor = conn.cursor()
#     cursor.execute("SELECT DISTINCT subject_name FROM admindb WHERE semester IN ({})".format(",".join(map(str, sem))))
#     subjects = cursor.fetchall()
#     return [subject[0] for subject in subjects]

def create_query(iteration):
    n = generate_random_number(len(col_header) - 1)
    if n==0:
    	col_header.pop(0)
    	return [-1,-1]

    col = col_header[n]
    res = ""
    rem_office = set()  # initialize

    # Check if the last tuple's last element in result_list is true
        # Your block of code here
    match col:
        case "department_name":
            # Check if any office location has been popped
            if len(office) != len(office_temp):
                rem_office = set(office) - set(office_temp)
            if rem_office:
                placeholders = ",".join(["?"] * len(rem_office))
                query = f"SELECT DISTINCT department_name FROM admindb WHERE office IN ({placeholders})"
                cursor.execute(query, tuple(rem_office))
                subs = cursor.fetchall()
                dept_temp[:] = [sub[0] for sub in subs if sub[0] in dept_temp]
            i = generate_random_number(len(dept_temp) - 1)
            res = dept_temp[i]
            col_header.pop(n)
        case "subject_name":
            i = generate_random_number(len(subject_temp) - 1)
            res = subject_temp[i]
            col_header.pop(n)
        case "gender":
            i = generate_random_number(len(gender_temp) - 1)
            res = gender_temp[i]
            col_header.pop(n)
        case "office":
            i = generate_random_number(len(office_temp) - 1)
            res = office_temp[i]
            col_header.pop(n)
        case "doctorate":
            i = generate_random_number(len(doc_temp) - 1)
            res = doc_temp[i]
            col_header.pop(n)
        case "year_of_study":
            i = generate_random_number(len(yos_temp) - 1)
            res = yos_temp[i]
            col_header.pop(n)
        case "semester":
            i = generate_random_number(len(semester_temp) - 1)
            res = semester_temp[i]
            col_header.pop(n)

    return [col, res]

