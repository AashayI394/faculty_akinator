import sqlite3

conn = sqlite3.connect('facinator.db')
cursor = conn.cursor()

update_query = """
UPDATE Facinator_MasterDB_Sheet1
SET office= 'AC'
WHERE department_id= '4.0';
"""

cursor.execute(update_query)

conn.commit()

conn.close()
