import sqlite3, random

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

def find_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = list(set1 & set2)
    return intersection

def facinator_game(col, res, val, g):
    if len(g.result) > 1:
        g.gametuple.append((col, res, val))
        print(g.gametuple)
        tempres = singlequery(col, res)
        if val == 'yes':
            if col in g.col_header:
                g.col_header.remove(col)
        if val == 'no':
            tempres = list(set(g.result) - set(tempres))
            g.delete_res(col, res)
        g.result = find_intersection(g.result, tempres)
    

class GameSession:
    def __init__(self):
        self.result = query_all()
        self.col_header = ["department_name","subject_name","gender","doctorate","office","year_of_study","semester"]
        # Call the update_params method
        self.update_params()
        self.gametuple = []
        self.question_thread = []
        self.col_res = []

    def update_params(self):
        # Original lists
        self.dept_temp = [t[3] for t in self.result]
        self.yos_temp = [t[7] for t in self.result]
        self.gender_temp = [t[9] for t in self.result]
        self.semester_temp = [t[8] for t in self.result]
        self.office_temp = [t[11] for t in self.result]
        self.doc_temp = [t[10] for t in self.result]
        self.subject_temp = [t[6] for t in self.result]

        # Removing duplicates from each list
        self.dept_temp = list(set(self.dept_temp))
        self.yos_temp = list(set(self.yos_temp))
        self.gender_temp = list(set(self.gender_temp))
        self.semester_temp = list(set(self.semester_temp))
        self.office_temp = list(set(self.office_temp))
        self.doc_temp = list(set(self.doc_temp))
        self.subject_temp = list(set(self.subject_temp))
    
    def create_query(self):
        self.update_params()
        if len(self.col_header) == 0:
            return [-1,-1]
        col = random.choice(self.col_header)
        # initiazlize res
        res = ""
        # Check if the last tuple's last element in result_list is true
            # Your block of code here
        match col:
            case "department_name":
                if not self.dept_temp:
                    self.create_query()
                else:
                    res = random.choice(self.dept_temp)
            case "subject_name":
                if not self.subject_temp:
                    self.create_query()
                else:
                    res = random.choice(self.subject_temp)
            case "gender":
                if not self.gender_temp:
                    self.create_query()
                else:
                    res = random.choice(self.gender_temp)
            case "office":
                if not self.office_temp:
                    self.create_query()
                else:
                    res = random.choice(self.office_temp)
            case "doctorate":
                if not self.doc_temp:
                    self.create_query()
                else:
                    res = random.choice(self.doc_temp)
            case "year_of_study":
                if not self.yos_temp:
                    self.create_query()
                else:
                    res = random.choice(self.yos_temp)
            case "semester":
                if not self.semester_temp:
                    self.create_query()
                else:
                    res = random.choice(self.semester_temp)
        return [col, res]
    
    def create_question(self,col,res):
        match col:
            case "department_name":
                q = "Does the Faculty belong to " + res + " department ?"
            case "subject_name":
                q = "Does this Faculty teach the course " + res +" ?"
            case "gender":
                q = "Is the Faculty "+ res +" ?"
            case "doctorate":
                if res == 'yes':
                    q = "Does this Faculty member have a PhD ?"
                if res == 'no':
                    q = "The Faculty does not hold a PhD ?"

            case "office":
                q = "Is this faculty's office located in the " + res +" ?"
            case "year_of_study":
                q = "Does this Faculty conduct any class year "+ str(res) + " ?"
            case "semester":
                q = "Does the Faculty teach any course of semester " + str(res) + " ?"
        return q

    def delete_res(self, col, res):
        match col:
            case "department_name":
                if res in self.dept_temp:
                    self.dept_temp.remove(res)
            case "subject_name":
                if res in self.subject_temp:
                    self.subject_temp.remove(res)
            case "gender":
                if res in self.gender_temp:
                    self.gender_temp.remove(res)
            case "office":
                if res in self.office_temp:
                    self.office_temp.remove(res)
            case "doctorate":
                if res in self.doc_temp:
                    self.doc_temp.remove(res)
            case "year_of_study":
                if res in self.yos_temp:
                    self.yos_temp.remove(res)
            case "semester":
                if res in self.semester_temp:
                    self.semester_temp.remove(res)
        return
   






# g = GameSession()

# print(g.result)

# gc = g.params()

# print(g.col_header)
# print(g.dept_temp)
# print(g.doc_temp)
# print(g.create_query())
# print(g.create_query())
# print(g.create_query())
# print(g.create_query())
# print(g.create_query())

# print(g.create_question())
# print(g.create_question())
# print(g.col_header)
# print("\n\n")




# facinator_game('department_name', 'Physics', 'yes', g)
# print(g.result)
# print(g.col_header)
# print(g.dept_temp)

# print("\n\n")
# facinator_game('gender', 'female', 'no', g)
# print(g.result)
# print(g.col_header)
# print(g.dept_temp)

