import hashlib

from database import DB

class User:
	def __init__(self, id, username, email, password):
		self.id = id
		self.username = username
		self.email = email
		self.password = password
	
	def create(self):
		with DB() as db:
			values = (self.username,self.email ,self.password)
			db.execute('''
				INSERT INTO users (Username, Email, Password)
				VALUES(?, ?, ?)''', values)
			return self
	
	@staticmethod
	def find_user(username):
		if not username:
			return None
		with DB() as db:
			row = db.execute(
				'SELECT * FROM users WHERE username = ?', (username,)
			).fetchone()
			if row:
				return User(*row)
	
	@staticmethod
	def hash_password(password):
		return hashlib.sha256(password.encode('utf-8')).hexdigest()
	
	def verify_password(self, password):
		return self.password == hashlib.sha256(password.encode('utf-8')).hexdigest()
