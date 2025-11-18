import sqlite3


conn = sqlite3.connect("../my_database.db")
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

cur.execute("CREATE INDEX idx_email ON Users (email)")

cur.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser', 'newuser@example.com', 28))

conn.commit()
conn.close()


