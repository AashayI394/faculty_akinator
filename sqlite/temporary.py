import sqlite3

conn = sqlite3.connect('temp.db')

cursor = conn.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS faculties (
#                     id INTEGER PRIMARY KEY,
#                     name TEXT NOT NULL,
#                     email TEXT,
#                     department_id INTEGER,
#                     subject_id INTEGER,
#                     FOREIGN KEY (department_id) REFERENCES departments(id),
#                     FOREIGN KEY (subject_id) REFERENCES subjects(id)
#                 )''')


#inserting faculties in faculties table
# many_faculties = [
#                     ('Dr. Shendge P. D.','pds.instru@coeptech.ac.in',8,32),
#                     ('Ms. Bhole K. A.','kab.instru@coeptech.ac.in',8,28),
#                     ('Dr. Agashe S. D.','sda.instru@coeptech.ac.in',8,29),
#                     ('Dr. Patil S. L.','slp.instru@coeptech.ac.in',8,30),
#                     ('Dr. Chaskar U. M.','umc.instru@coeptech.ac.in',8,31),
#                     ('Dr. Patil C. Y.','cyp.instru@coeptech.ac.in',8,33),
#                     ('Dr. Chaskar U. M.','umc.instru@coeptech.ac.in',8,34),
#                     ]

# cursor.executemany("INSERT INTO faculties (name,email,department_id,subject_id) VALUES (?,?,?,?)",many_faculties)
# print("Faculties added...")

# cursor.execute("SELECT * FROM faculties")
# items = cursor.fetchall()

# for i in items:
# 	print(i[1]+" | "+i[2]+" | "+str(i[3])+" | "+str(i[4]))

#inserting another column in the table
# genders = [
# 			('Male'),
# 			('Female'),
# 			('Male'),
# 			('Male'),
# 			('Male'),
# 			('Male'),
# 			('Male'),
# 			]

# cursor.execute('''ALTER TABLE faculties
# 				  ADD COLUMN gender TEXT
# 						''')

# for gender in genders:
# 	cursor.execute("UPDATE faculties SET gender = ? WHERE rowid = (SELECT MIN(rowid) FROM faculties WHERE gender IS NULL)", gender[0],)

# cursor.execute("UPDATE faculties SET gender = 'Male' WHERE gender = 'M'")
# print("Male changed")
# cursor.execute("UPDATE faculties SET gender = 'Female' WHERE gender = 'F'")
# print("Female changed")
# conn.commit()
cursor.execute("SELECT * FROM faculties")

fac= cursor.fetchall()
print("Number of rows fetched: ",len(fac))
for i in fac:
	print("Name: ",i[1])
	print("Email: ",i[2])
	print("Gender: ",i[5])
	print()


# cursor.executemany("UPDATE faculties SET gender = ?", genders)
# print("Genders added")
# conn.commit()
conn.close()