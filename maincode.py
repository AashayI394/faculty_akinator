import sqlite3, random
from guesslogic import generate_random_number, find_intersection, create_query, singlequery, query_all, dept_temp, yos_temp, gender_temp, semester_temp, doc_temp, office_temp,subject_temp

conn = sqlite3.connect('facinator.db')
cursor = conn.cursor()


result = query_all()

def facinator_game():
	global result
	while(len(result)>1):
		intermediate = create_query()  #intermediate is a list of length two
		print(intermediate)
		print()
		tempres = singlequery(intermediate[0],intermediate[1])
		result = find_intersection(result, tempres)
		print(result)
		print("\n\n\n")
	return result


testcase = facinator_game()
