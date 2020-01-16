from database import DB

class Image:
	def __init__(self, id, name, catagory):
		self.id = id
		self.name = name
		self.catagory = catagory
	
	def create(self):
		with DB as db():
			values = (self.name, self.catagory)
			db.execute('''
				INSERT INTO images (Name, Catagory)
				VALUES(?, ?)''', values)
			return self
	
	@staticmethod
	def all():
		with DB() as db:
			rows = db.execute('SELECT * FROM images').fetchall()
			return [Image(*row) for row in rows]

	@staticmethod
	def find_by_catagory(catagory):
		with DB() as db:
			rows = db.execute('SELECT * FROM images WHERE catagory = ?', (catagory,)).fetchall()
			if not rows:
				return None
			return [Image(*row) for row in rows]
	
	@staticmethod
	def find_by_id(id):
		with DB() as db:
			row = db.execute('SELECT * FROM images WHERE id = ?', (id,)).fetchone()
			if not row:
				return None
			return Image(*row)
	
	def printInfo(self):
		print(self.id)
		print(self.name)
		print(self.catagory)
		print("-------")
