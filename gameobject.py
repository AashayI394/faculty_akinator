import sqlite3, random

def query_all():
    conn = sqlite3.connect('facinator.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM admindb")
    result = cursor.fetchall()
    return result
    conn.close() 

def create_query(p,):
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
            res = random.choice(dept_temp)
        case "subject_name":
            res = random.choice(subject_temp)
        case "gender":
            res = random.choice(gender_temp)
        case "office":
            res = random.choice(office_temp)
        case "doctorate":
            res = random.choice(doc_temp)
        case "year_of_study":
            res = random.choice(yos_temp)
        case "semester":
            res = random.choice(semester_temp)
    return [col, res]


    

class GameSession:
    def __init__(self):
        self.result = query_all()
        self.col_header = ["department_name","subject_name","gender","doctorate","office","year_of_study","semester"]
        # Call the update_params method
        self.update_params()

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
        if len(self.col_header) == 0:
            return [-1,-1]
        col = random.choice(self.col_header)
        # initiazlize res
        res = ""
        # Check if the last tuple's last element in result_list is true
            # Your block of code here
        match col:
            case "department_name":
                res = random.choice(self.dept_temp)
            case "subject_name":
                res = random.choice(self.subject_temp)
            case "gender":
                res = random.choice(self.gender_temp)
            case "office":
                res = random.choice(self.office_temp)
            case "doctorate":
                res = random.choice(self.doc_temp)
            case "year_of_study":
                res = random.choice(self.yos_temp)
            case "semester":
                res = random.choice(self.semester_temp)
        return [col, res]
    
    def create_question(self):
        col,res = self.create_query()
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





g = GameSession()

# print(g.result)

# gc = g.params()

print(g.col_header)
print(g.dept_temp)
print(g.doc_temp)
print(g.create_query())
print(g.create_query())
print(g.create_query())
print(g.create_query())
print(g.create_query())

print(g.create_question())
print(g.create_question())

