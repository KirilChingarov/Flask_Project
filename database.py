import sqlite3

DB_NAME = "database.db"

conn = sqlite3.connect(DB_NAME)

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS users
	(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	Username TEXT,
	Email TEXT,
	Password TEXT
	)
''')

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS catagories
	(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	Name TEXT
	)
''')

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS images
	(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	Name TEXT,
	Catagory INTEGER
	)
''')

class DB:
	def __enter__(self):
		self.conn = sqlite3.connect(DB_NAME)
		return self.conn.cursor()
	
	def __exit__(self, type, value, traceback):
		self.conn.commit()
