import sqlite3, random


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



cursor.execute("SELECT DISTINCT semester FROM admindb")
subs = cursor.fetchall()
semester = []
for sub in subs:
    semester.append(sub[0])
    semester_temp = semester


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


def generate_random_number(upper_limit):
    return random.randint(1, upper_limit)

def find_intersection(list1, list2):
    # Convert lists to sets for easy intersection calculation
    set1 = set(list1)
    set2 = set(list2)
   
    # Calculate intersection using the '&' operator
    intersection = list(set1 & set2)
    
    return intersection


def create_query():
	n = generate_random_number(len(col_header)-1)
	col= col_header[n]
	res=""
	match col:
		case "department_name":
			i = generate_random_number(len(dept_temp)-1)
			res = dept_temp[i]
			dept_temp.pop(i)
		case "subject_name":
			i = generate_random_number(len(subject_temp)-1)
			res = subject_temp[i]
			subject_temp.pop(i)
		case "gender":
			i = generate_random_number(len(gender_temp)-1)
			res = gender_temp[i]
			gender_temp.pop(i)
			col_header.pop(n)
		case "office":
			i = generate_random_number(len(office_temp)-1)
			res = office_temp[i]
			office_temp.pop(i)
		case "doctorate":
			i = generate_random_number(len(doc_temp)-1)
			res = doc_temp[i]
			doc_temp.pop(i)
			col_header.pop(n)
		case "year_of_study":
			i = generate_random_number(len(yos_temp)-1)
			res = yos_temp[i]
			yos_temp.pop(i)
			col_header.pop(n)
		case "semester":
			i = generate_random_number(len(semester_temp)-1)
			res = semester_temp[i]
			semester_temp.pop(i)
			col_header.pop(n)
	return [col,res]



# result = query_all()
# print("obtained whole list")

# col1 = "department_name"
# res1 = "Computer Engineering"
# ans = singlequery(col1,res1) 
# print(ans)
# print()
# new_result = [t for t in result if t in ans]
# result = new_result
# print(result)


# print("\n\n")

# col2 = "gender"
# res2 = "female"
# ans = singlequery(col2,res2) 
# print(ans)
# print()
# new_result = [t for t in result if t in ans]
# result = new_result
# print(result)























# def guess_faculty():
# 	criteria = []
#     if request.form.get('subject_name'):
#         criteria.append(f"subject_name = '{request.form['subject_name']}'")
#     if request.form.get('gender'):
#         criteria.append(f"gender = '{request.form['gender']}'")
#     if request.form.get('doctorate'):
#         criteria.append(f"doctorate = '{request.form['doctorate']}'")
#     if request.form.get('office'):
#         criteria.append(f"office = '{request.form['office']}'")
#     if request.form.get('year_of_study'):
#         criteria.append(f"year_of_study = '{request.form['year_of_study']}'")
    
#     result = query_faculty(criteria)
#     if len(result) == 1:
#         faculty = result[0]
#         return render_template('result.html', faculty=faculty)
#     else:
#         return render_template('retry.html')


# # Simulate user input (example criteria)
# criteria = []
# criteria.append("subject_name = 'Computer Engineering'")
# criteria.append("gender = 'female'")
# criteria.append("doctorate = 'yes'")
# criteria.append("office = 'Academic Complex'")
# criteria.append("year_of_study = 2")

# result = query_faculty(criteria)
# # if len(result) == 1:
# # 	faculty = result[0]
# # 	print("Found Faculty: ",faculty)
# # else:
# # 	print("No faculty found.")
# print(result)
