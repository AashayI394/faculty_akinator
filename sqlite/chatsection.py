import sqlite3

# Connect to a SQLite database
conn = sqlite3.connect('chat.db')

# Create a cursor object
cur = conn.cursor()

# Write an SQL query to create a table
create_table_query = '''
CREATE TABLE IF NOT EXISTS faq (
    id INTEGER PRIMARY KEY,
    question TEXT NOT NULL,
    answer TEXT
);
'''

# Execute the SQL command
cur.execute(create_table_query)

# Inserting a single row
insert_query = '''INSERT INTO faq (question, answer) VALUES (?, ?);'''
data = ('What is Faculty Akinator or Facinator ?', 'Faculty Akinator (or Facinator) is a faculty recommendation system with a personalized "guess who?" game for students of COEP Tech ')
cur.execute(insert_query, data)

# Inserting multiple rows
users_data = [
    ('Does Facinator takes inspiration from the famous game Akinator ?', 'Yes! Facinator is based on the online french video game - Akinator which attempts to determine what fictional or real-life character, object, or animal the player is thinking of by asking a series of questions.'),
    ('How accurate is Facinator ?', "Facinator's accuracy depends on the information provided in its database and the questions asked during the game. The more specific and accurate your responses, the more likely it is to guess/recommend the faculty member you seek."),
    ('Can I suggest new faculty members to be added to Facinator ?', "Yes, we encourage suggestions for new faculty members to be added to Facinator. Simply fill out the form 'Help Us !' section with the name and some distinctive features of the faculty member, and our webapp auto=includes them in the database."),
    ("I'm having trouble with Facinator. Who can I contact for help?", "If you are experiencing any issues with Facinator or have questions about how to play, please reach out to our support team mentioned in our footer. We are here to help troubleshoot any problems and ensure you have a great user experience.")
]
cur.executemany(insert_query, users_data)

# Commit changes
conn.commit()

# Close connection
conn.close()
