import hashlib

from database import DB

class User:
	def __init__(self, first_name, last_name, email, password):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password
	
	def create(self):
		with DB() as db:
			values = (self.first_name ,self.last_name ,self.email ,self.password)
			db.execute('''
				INSERT INTO users (FirstName, LastName, Email, Password)
				VALUES(?, ?, ?, ?)''', values)
			return self
	
	@staticmethod
	def hash_password(password):
		return hashlib.sha256(password.encode('utf-8')).hexdigest()
	
	def verify_password(self, password):
		return self.password == hashlib.sha256(password.encode('utf-8')).hexdigest()
