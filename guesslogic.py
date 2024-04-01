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

# dept_temp = []
# subject_temp = []
# yos_temp = []
# semester_temp = []
# gender_temp = []
# office_temp = []
# doc_temp = [] 
# col_header = []


# def game_reload():
        
# global dept_temp, subject_temp, yos_temp, semester_temp, gender_temp, office_temp,doc_temp
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

semester = [1,2,3,4,5,6,7,8]
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

def update_params(sliced_result):
    global dept_temp, yos_temp, gender_temp, semester_temp, doc_temp, office_temp,subject_temp
    dept_temp = [t[3] for t in sliced_result]
    yos_temp = [t[7] for t in sliced_result]
    gender_temp = [t[9] for t in sliced_result]
    semester_temp = [t[8] for t in sliced_result]
    office_temp = [t[11] for t in sliced_result]
    doc_temp = [t[10] for t in sliced_result]
    subject_temp = [t[6] for t in sliced_result]


def delete_query(col,res):
    
    match col:
        case "department_name":
            global dept_temp
            dept_temp.remove(res)
        case "subject_name":
            global subject_temp
            subject_temp.remove(res)
        case "office":
            global office_temp
            office_temp.remove(res)
        case "year_of_study":
            global yos_temp
            yos_temp.remove(res)
        case "doctorate":
            global doc_temp
            doc_temp.remove(res)
        case "semester":
            global semester_temp
            semester_temp.remove(res)
        case "gender":
            global gender_temp
            gender_temp.remove(res)
      
def create_query(p):
    n_temp = random.choice(col_header)

    n = col_header.index(n_temp)
    if len(col_header) == 0:
    	return [-1,-1]
    col = col_header[n]
    res = ""
    rem_office = set()  # initialize

    # Check if the last tuple's last element in result_list is true
        # Your block of code here
    match col:
        case "department_name":
            # dept_temp[:] = [sub[0] for sub in subs if sub[0] in dept_temp]
        # i = generate_random_number(len(dept_temp) - 1)
        # res = dept_temp[i]
            res = random.choice(dept_temp)
        case "subject_name":
            # i = generate_random_number(len(subject_temp) - 1)
            # res = subject_temp[i]
            res = random.choice(subject_temp)
        case "gender":
            # i = generate_random_number(len(gender_temp) - 1)
            # res = gender_temp[i]
            res = random.choice(gender_temp)
        case "office":
            # i = generate_random_number(len(office_temp) - 1)
            # res = office_temp[i]
            res = random.choice(office_temp)
        case "doctorate":
            # i = generate_random_number(len(doc_temp) - 1)
            # res = doc_temp[i]
            res = random.choice(doc_temp)
        case "year_of_study":
            # i = generate_random_number(len(yos_temp) - 1)
            # res = yos_temp[i]
            res = random.choice(yos_temp)
        case "semester":
            # i = generate_random_number(len(semester_temp) - 1)
            # res = semester_temp[i]
            res = random.choice(semester_temp)

    return [col, res]


