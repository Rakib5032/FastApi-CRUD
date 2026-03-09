import sqlite3

conn = sqlite3.connect('database\database.db', check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
student_id TEXT UNIQUE,
name TEXT,
email TEXT UNIQUE,
password TEXT, 
dept TEXT,
year TEXT,
phone TEXT,
address TEXT
)
""")

# cursor.execute("""
# INSERT INTO students(student_id, name, email, password, dept, year, phone, address)
# VALUES(?, ?, ?, ?, ?, ?, ?, ?)
# """, (
# "221",
# "Rakib Bhuiyan",
# "rabbi@gmail.com",
# "123456",
# "CSE", 
# "4",
# "01532342423",
# "Dhaka"
# ))

conn.commit()

# cursor.execute("SELECT * FROM students")
# rows = cursor.fetchall()

# for row in rows:
#     print(row)