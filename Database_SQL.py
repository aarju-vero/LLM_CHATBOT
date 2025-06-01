import sqlite3

conn=sqlite3.connect('chatbot.db')   # Create a conn to the database
cursor=conn.cursor() # Create a cursor object to execute SQL commands

# Create a table or table for chatbot as database
cursor.execute('''CREATE TABLE IF NOT EXISTS chatbot_table(
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    gender TEXT, 
    location TEXT)''')

cursor.execute('''INSERT INTO chatbot_table (name,gender,location) VALUES ("Riya","Female"," Greater Noida")''')
cursor.execute('''INSERT INTO chatbot_table (name,gender,location) VALUES ("Kalyani","Female","Varanasi")''')
cursor.execute('''INSERT INTO chatbot_table (name,gender,location) VALUES ("Hemant","Male","Badayun")''')
cursor.execute('''INSERT INTO chatbot_table (name,gender,location) VALUES ("Vivek","Male","Azamgarh")''')
cursor.execute('''INSERT INTO chatbot_table (name,gender,location) VALUES ("Ankit","Male","Kanpur")''')

conn.commit()
conn.close()

