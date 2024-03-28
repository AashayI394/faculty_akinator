import sqlite3, random
from guesslogic import generate_random_number, find_intersection, create_query, singlequery, query_all, dept_temp, yos_temp, gender_temp, semester_temp, doc_temp, office_temp,subject_temp

conn = sqlite3.connect('facinator.db')
cursor = conn.cursor()


result = query_all()

gametuple=[]

def facinator_game(col,res,val):
	global result
	global gametuple
	if len(result)>1:
		gametuple.append((col,res,val))
		tempres = singlequery(col,res)
		if not val:
			tempres = list(set(result) - set(tempres))
		result = find_intersection(result, tempres)

